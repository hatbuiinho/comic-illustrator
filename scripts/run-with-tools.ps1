[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Command
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot

& (Join-Path $PSScriptRoot "bootstrap-windows.ps1")

$env:Path = @(
    (Join-Path $ProjectRoot ".tools\bin"),
    (Join-Path $ProjectRoot ".venv\Scripts"),
    "C:\msys64\ucrt64\bin",
    $env:Path
) -join ";"

if ($Command -and $Command.Count -gt 0 -and $Command[0] -eq "--") {
    $Command = if ($Command.Count -gt 1) { $Command[1..($Command.Count - 1)] } else { @() }
}

if (-not $Command -or $Command.Count -eq 0) {
    Write-Host "Toolchain đã sẵn sàng. Không có lệnh cần chạy."
    exit 0
}

$executable = $Command[0]
$arguments = if ($Command.Count -gt 1) { $Command[1..($Command.Count - 1)] } else { @() }
& $executable @arguments
exit $LASTEXITCODE
