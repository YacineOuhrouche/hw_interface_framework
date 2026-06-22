# analyzes signal noise using sample statistics

import statistics


class NoiseAnalyzer:
    # stores noise analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # calculates the mean value of samples
    def calculate_mean(self, samples):
        return statistics.mean(samples)

    # calculates peak to peak noise
    def calculate_peak_to_peak(self, samples):
        return max(samples) - min(samples)

    # calculates standard deviation noise
    def calculate_standard_deviation(self, samples):
        return statistics.pstdev(samples)

    # calculates peak noise from the mean
    def calculate_peak_noise(self, samples):
        mean_value = self.calculate_mean(samples)

        return max(abs(sample - mean_value) for sample in samples)

    # analyzes noise from samples
    def analyze(self, samples):
        return {
            "analysis": "noise",
            "sample_count": len(samples),
            "mean": self.calculate_mean(samples),
            "peak_to_peak": self.calculate_peak_to_peak(samples),
            "standard_deviation": self.calculate_standard_deviation(samples),
            "peak_noise": self.calculate_peak_noise(samples),
        }