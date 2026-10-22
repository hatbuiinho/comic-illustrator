const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { spawnSync } = require("node:child_process");
const script = path.resolve(__dirname, "../scripts/validate-visual-qa.js");
const pass = evidence => ({ status: "PASS", evidence });
const fail = () => ({ status: "FAIL", evidence: "Môi có nhiều lớp bóng mô phỏng thể tích.", remediation: "Gom bóng phụ, giữ đường môi.", preserve: "Giữ mắt, mày và thiết kế trang phục.", retryable: true });
function base() {
  return {
    schemaVersion: 2, output: "candidate.svg", deliverableType: "studio-profile", hasCharacters: true,
    checks: { style: pass("Các vùng đang có dùng nét và mảng cel."), profile: pass("Mắt/mày và dấu riêng đã đối chiếu nguồn.") },
    styleConsistencyByElement: Object.fromEntries(["faceSkin", "hair", "fabric", "jewelry", "background"].map(name => [name, pass(`Đã xem nhóm ${name}, không thấy drift.`)]))
  };
}
function run(data) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "visual-report-test-"));
  try {
    fs.writeFileSync(path.join(dir, "candidate.svg"), '<svg xmlns="http://www.w3.org/2000/svg"/>');
    fs.writeFileSync(path.join(dir, "qa.json"), typeof data === "string" ? data : JSON.stringify(data));
    const r = spawnSync(process.execPath, [script, path.join(dir, "qa.json")], { encoding: "utf8" });
    assert.ok(r.stdout, r.stderr);
    return { exit: r.status, ...JSON.parse(r.stdout) };
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
}
test("studio profile đạt không cần gate trang truyện", () => {
  const r = run(base()); assert.equal(r.exit, 0); assert.equal(r.qaOutcome, "PASS"); assert.equal(r.eligibleForNextStep, true);
  assert.ok(!r.requiredChecks.includes("storytelling"));
});
test("không có checks không thể đi tiếp", () => {
  const d = base(); delete d.checks; const r = run(d);
  assert.equal(r.exit, 1); assert.equal(r.reportValidity, "FAIL"); assert.equal(r.eligibleForNextStep, false);
});
test("report hợp lệ chứa FAIL không thành QA PASS", () => {
  const d = base(); d.checks.style = fail(); d.styleConsistencyByElement.faceSkin = { status: "FAIL", evidence: "Môi tạo khối render." };
  const r = run(d); assert.equal(r.exit, 2); assert.equal(r.reportValidity, "PASS"); assert.equal(r.qaOutcome, "FAIL"); assert.equal(r.eligibleForNextStep, false);
});
test("không bỏ được check preset bằng requiredChecks rỗng", () => {
  const d = base(); d.requiredChecks = []; delete d.checks.profile; assert.equal(run(d).exit, 1);
});
test("PASS thiếu bằng chứng bị từ chối", () => {
  const d = base(); d.checks.profile = { status: "PASS" }; assert.equal(run(d).exit, 1);
});
test("nhóm mặt FAIL mâu thuẫn style tổng PASS bị từ chối", () => {
  const d = base(); d.styleConsistencyByElement.faceSkin = { status: "FAIL", evidence: "Bóng quanh mũi liên tục." }; assert.equal(run(d).exit, 1);
});
test("không thể bỏ nhóm kiểm mặt", () => {
  const d = base(); delete d.styleConsistencyByElement.faceSkin; assert.equal(run(d).exit, 1);
});
test("waiver thiếu scope hoặc nguồn user không hợp lệ", () => {
  for (const field of ["scope", "authorizationSource"]) {
    const d = base(); d.checks.profile = { status: "SKIPPED_BY_USER", reason: "Test có kiểm soát", scope: "profile/candidate.svg/studio-profile", authorizationSource: "Yêu cầu user trong test" };
    delete d.checks.profile[field]; assert.equal(run(d).exit, 1);
  }
});
test("waiver có nguồn được phân biệt với PASS toàn bộ", () => {
  const d = base(); d.checks.profile = { status: "SKIPPED_BY_USER", reason: "Chỉ test style", scope: "profile/candidate.svg/studio-profile", authorizationSource: "User yêu cầu test style dù còn lỗi mặt" };
  const r = run(d); assert.equal(r.exit, 0); assert.equal(r.qaOutcome, "PASS_WITH_WAIVERS"); assert.deepEqual(r.waivedChecks, ["profile"]);
});
test("N/A không thay được identity bắt buộc", () => {
  const d = base(); d.checks.profile = { status: "NOT_APPLICABLE", reason: "Không muốn kiểm" }; assert.equal(run(d).exit, 1);
});
test("ảnh không có nhân vật không cần profile hoặc các nhóm mặt", () => {
  const d = { schemaVersion: 2, output: "candidate.svg", deliverableType: "studio-image", hasCharacters: false, checks: { style: pass("Vật thể dùng mảng 2D.") }, styleConsistencyByElement: { subject: pass("Nét/mảng rõ."), background: { status: "NOT_APPLICABLE", reason: "Nền trắng không có cảnh." } } };
  const r = run(d); assert.equal(r.exit, 0); assert.ok(!r.requiredChecks.includes("profile"));
});
test("trang truyện không dùng preset studio để bỏ scope đã khai", () => {
  const d = base(); d.deliverableType = "comic-page"; assert.equal(run(d).exit, 1);
});
test("JSON lỗi và input stale trả kết quả không đủ điều kiện", () => {
  assert.equal(run("{bad").exit, 1); const d = base(); d.inputStatus = "STALE"; assert.equal(run(d).eligibleForNextStep, false);
});
test("performance FAIL không bị bỏ qua trong QA tổng", () => {
  const d = base(); d.requiresPerformanceCoherence = true;
  d.performanceReadByCharacter = { a: { intendedRead: "bình tĩnh", observedRead: "giận", status: "FAIL", conflictingSignals: "Mày cau", remediation: "Sửa biểu cảm" } };
  d.groupEmotionalCoherence = { status: "PASS" };
  const r = run(d); assert.equal(r.exit, 2); assert.equal(r.qaOutcome, "FAIL");
});
