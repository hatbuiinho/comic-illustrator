[CmdletBinding()]
param(
    [switch]$CheckOnly,
    [switch]$ForceRefresh
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

if ($env:OS -ne "Windows_NT") {
    throw "Script này chỉ dùng cho Windows."
}

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$ManifestPath = Join-Path $ProjectRoot ".tools\windows-tools.json"
$StatePath = Join-Path $ProjectRoot ".tools\state.windows.json"
$RequirementsPath = Join-Path $ProjectRoot "requirements-tools.txt"
$VenvPath = Join-Path $ProjectRoot ".venv"
$VenvPython = Join-Path $VenvPath "Scripts\python.exe"
$LocalBin = Join-Path $ProjectRoot ".tools\bin"

function Refresh-ProcessPath {
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $extra = @(
        $LocalBin,
        (Join-Path $VenvPath "Scripts"),
        "C:\msys64\ucrt64\bin"
    )

    $popplerBins = Get-ChildItem "C:\Program Files" -Directory -Filter "poppler*" -ErrorAction SilentlyContinue |
        ForEach-Object {
            @(
                (Join-Path $_.FullName "Library\bin"),
                (Join-Path $_.FullName "bin")
            )
        }

    $env:Path = (@($extra) + @($popplerBins) + @($machinePath, $userPath)) -join ";"
}

function Test-AnyCommand([string[]]$Names) {
    foreach ($name in $Names) {
        if (Get-Command $name -ErrorAction SilentlyContinue) { return $true }
    }
    return $false
}

function Test-AllCommands([string[]]$Names) {
    foreach ($name in $Names) {
        if (-not (Get-Command $name -ErrorAction SilentlyContinue)) { return $false }
    }
    return $true
}

function Install-WingetPackage($Tool) {
    $commandsReady = if ($Tool.name -eq "Python 3.12") {
        Test-AnyCommand $Tool.commands
    } else {
        Test-AllCommands $Tool.commands
    }
    if ($Tool.commands.Count -gt 0 -and $commandsReady) {
        Write-Host "[OK] $($Tool.name)"
        return
    }

    if ($Tool.name -eq "MSYS2" -and (Test-Path "C:\msys64\usr\bin\bash.exe")) {
        Write-Host "[OK] MSYS2"
        return
    }

    if ($CheckOnly) {
        throw "Thiếu $($Tool.name) ($($Tool.id)). Chạy lại không có -CheckOnly để cài."
    }

    Write-Host "[INSTALL] $($Tool.name)"
    & winget install --id $Tool.id --exact --accept-package-agreements --accept-source-agreements --silent
    if ($LASTEXITCODE -ne 0) {
        throw "winget không cài được $($Tool.name) ($($Tool.id)); exit code $LASTEXITCODE."
    }
    Refresh-ProcessPath
}

function Get-CommandVersion([string]$Name) {
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if (-not $command) { return $null }
    try {
        $line = (& $command.Source --version 2>&1 | Select-Object -First 1).ToString().Trim()
        return @{ path = $command.Source; version = $line }
    } catch {
        return @{ path = $command.Source; version = "installed" }
    }
}

if (-not (Test-Path $ManifestPath)) {
    throw "Không tìm thấy manifest: $ManifestPath"
}
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw "Thiếu winget. Hãy cài hoặc cập nhật Microsoft App Installer, rồi chạy lại script."
}

Refresh-ProcessPath
$manifest = Get-Content $ManifestPath -Raw | ConvertFrom-Json

foreach ($tool in $manifest.winget) {
    Install-WingetPackage $tool
}

$bash = "C:\msys64\usr\bin\bash.exe"
foreach ($tool in $manifest.msys2) {
    if (-not (Test-AnyCommand $tool.commands)) {
        if ($CheckOnly) {
            throw "Thiếu $($Tool.name) ($($tool.package)). Chạy lại không có -CheckOnly để cài."
        }
        Write-Host "[INSTALL] $($tool.name) qua MSYS2"
        & $bash -lc "pacman -Sy --needed --noconfirm $($tool.package)"
        if ($LASTEXITCODE -ne 0) {
            throw "MSYS2 không cài được $($tool.package); exit code $LASTEXITCODE."
        }
        Refresh-ProcessPath
    } else {
        Write-Host "[OK] $($tool.name)"
    }
}

if (-not (Test-Path $VenvPython)) {
    if ($CheckOnly) { throw "Thiếu môi trường Python .venv. Chạy lại không có -CheckOnly để tạo." }
    Write-Host "[CREATE] .venv"
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3.12 -m venv $VenvPath
    } else {
        & python -m venv $VenvPath
    }
    if ($LASTEXITCODE -ne 0) { throw "Không tạo được .venv." }
}

$requirementsHash = (Get-FileHash $RequirementsPath -Algorithm SHA256).Hash
$previousState = $null
if (Test-Path $StatePath) {
    try { $previousState = Get-Content $StatePath -Raw | ConvertFrom-Json } catch { $previousState = $null }
}
$pythonReady = $previousState -and
    $previousState.requirementsSha256 -eq $requirementsHash -and
    -not $ForceRefresh

if ($pythonReady) {
    & $VenvPython -c "import yaml, PIL, pdfplumber, pypdf, reportlab" 2>$null
    $pythonReady = $LASTEXITCODE -eq 0
}

if (-not $pythonReady) {
    if ($CheckOnly) { throw "Python requirements chưa đồng bộ. Chạy lại không có -CheckOnly để cài." }
    Write-Host "[SYNC] Python requirements"
    & $VenvPython -m pip install --upgrade pip
    & $VenvPython -m pip install --requirement $RequirementsPath
    if ($LASTEXITCODE -ne 0) { throw "Không cài được Python requirements." }
}

New-Item -ItemType Directory -Force -Path $LocalBin | Out-Null
$pythonShim = Join-Path $LocalBin "python3.cmd"
$shimContent = "@echo off`r`n`"%~dp0..\..\.venv\Scripts\python.exe`" %*`r`n"
[IO.File]::WriteAllText($pythonShim, $shimContent, [Text.Encoding]::ASCII)
Refresh-ProcessPath

$requiredCommands = @("git", "node", "rg", "pdfinfo", "pdftotext", "pdftoppm", "rsvg-convert", "python3")
$commandState = [ordered]@{}
foreach ($name in $requiredCommands) {
    $details = Get-CommandVersion $name
    if (-not $details) { throw "Sau bootstrap vẫn thiếu command bắt buộc: $name" }
    $commandState[$name] = $details
}

$state = [ordered]@{
    schemaVersion = 1
    checkedAt = (Get-Date).ToString("o")
    machine = $env:COMPUTERNAME
    manifestSha256 = (Get-FileHash $ManifestPath -Algorithm SHA256).Hash
    requirementsSha256 = $requirementsHash
    venvPython = $VenvPython
    commands = $commandState
}
$state | ConvertTo-Json -Depth 6 | Set-Content -Path $StatePath -Encoding UTF8

Write-Host "[READY] Toolchain đã sẵn sàng. State: $StatePath"
