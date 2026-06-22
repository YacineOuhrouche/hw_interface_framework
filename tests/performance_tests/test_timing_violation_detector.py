# tests timing violation detector behavior

from diagnostics.timing_violation_detector import TimingViolationDetector


# verifies one timing violation is detected
def test_detect_violation_true():
    detector = TimingViolationDetector(timing_limit=10)

    result = detector.detect_violation(15)

    assert result is True


# verifies one timing value passes
def test_detect_violation_false():
    detector = TimingViolationDetector(timing_limit=10)

    result = detector.detect_violation(5)

    assert result is False


# verifies multiple timing violations are detected
def test_detect_violations():
    detector = TimingViolationDetector(timing_limit=10)

    result = detector.detect_violations([5, 15, 8, 20])

    assert len(result) == 2
    assert result[0]["index"] == 1
    assert result[1]["index"] == 3


# verifies summary passes when there are no violations
def test_timing_violation_summary_passes():
    detector = TimingViolationDetector(timing_limit=10)

    result = detector.summarize([1, 2, 3])

    assert result["passed"] is True
    assert result["violation_count"] == 0


# verifies summary fails when there are violations
def test_timing_violation_summary_fails():
    detector = TimingViolationDetector(timing_limit=10)

    result = detector.summarize([1, 20, 3])

    assert result["passed"] is False
    assert result["violation_count"] == 1