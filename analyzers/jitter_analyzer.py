# analyzes timing jitter from period measurements


class JitterAnalyzer:
    # stores jitter analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # calculates average period
    def calculate_average_period(self, periods):
        return sum(periods) / len(periods)

    # calculates peak to peak jitter
    def calculate_peak_to_peak_jitter(self, periods):
        return max(periods) - min(periods)

    # calculates maximum absolute jitter from average period
    def calculate_max_absolute_jitter(self, periods):
        average_period = self.calculate_average_period(periods)

        return max(abs(period - average_period) for period in periods)

    # analyzes jitter measurements
    def analyze(self, periods):
        return {
            "analysis": "jitter",
            "sample_count": len(periods),
            "average_period": self.calculate_average_period(periods),
            "peak_to_peak_jitter": self.calculate_peak_to_peak_jitter(periods),
            "max_absolute_jitter": self.calculate_max_absolute_jitter(periods),
        }