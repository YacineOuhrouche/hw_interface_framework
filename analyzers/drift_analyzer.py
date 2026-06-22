# analyzes signal drift over time


class DriftAnalyzer:
    # stores drift analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # calculates total drift from first sample to last sample
    def calculate_total_drift(self, samples):
        return samples[-1] - samples[0]

    # calculates absolute drift from first sample to last sample
    def calculate_absolute_drift(self, samples):
        return abs(self.calculate_total_drift(samples))

    # calculates drift rate per sample
    def calculate_drift_rate_per_sample(self, samples):
        if len(samples) <= 1:
            return 0.0

        return self.calculate_total_drift(samples) / (len(samples) - 1)

    # analyzes drift from samples
    def analyze(self, samples):
        return {
            "analysis": "drift",
            "sample_count": len(samples),
            "start_value": samples[0],
            "end_value": samples[-1],
            "total_drift": self.calculate_total_drift(samples),
            "absolute_drift": self.calculate_absolute_drift(samples),
            "drift_rate_per_sample": self.calculate_drift_rate_per_sample(samples),
        }