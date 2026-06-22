# analyzes timing measurements and response times


class TimingAnalyzer:
    # stores timing analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # calculates average timing value
    def calculate_average_time(self, timings):
        return sum(timings) / len(timings)

    # calculates minimum timing value
    def calculate_min_time(self, timings):
        return min(timings)

    # calculates maximum timing value
    def calculate_max_time(self, timings):
        return max(timings)

    # calculates timing spread
    def calculate_spread(self, timings):
        return max(timings) - min(timings)

    # analyzes timing measurements
    def analyze(self, timings):
        return {
            "analysis": "timing",
            "sample_count": len(timings),
            "average_time": self.calculate_average_time(timings),
            "minimum_time": self.calculate_min_time(timings),
            "maximum_time": self.calculate_max_time(timings),
            "spread": self.calculate_spread(timings),
        }