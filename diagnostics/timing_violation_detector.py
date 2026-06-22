# detects timing violations from measured timing values


class TimingViolationDetector:
    # stores timing violation limits
    def __init__(self, timing_limit):
        self.timing_limit = timing_limit

    # checks one timing measurement for violation
    def detect_violation(self, measured_time):
        return measured_time > self.timing_limit

    # checks multiple timing measurements for violations
    def detect_violations(self, measured_times):
        violations = []

        for index, measured_time in enumerate(measured_times):
            if self.detect_violation(measured_time):
                violations.append(
                    {
                        "index": index,
                        "measured_time": measured_time,
                        "limit": self.timing_limit,
                    }
                )

        return violations

    # summarizes timing violations
    def summarize(self, measured_times):
        violations = self.detect_violations(measured_times)

        return {
            "test": "timing_violation",
            "passed": len(violations) == 0,
            "sample_count": len(measured_times),
            "violation_count": len(violations),
            "limit": self.timing_limit,
            "violations": violations,
        }