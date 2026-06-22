# analyzes signal saturation and clipping behavior


class SaturationAnalyzer:
    # stores saturation analyzer settings
    def __init__(self, config=None):
        self.config = config or {}

    # counts samples at or below the minimum limit
    def count_low_saturation(self, samples, minimum):
        return sum(1 for sample in samples if sample <= minimum)

    # counts samples at or above the maximum limit
    def count_high_saturation(self, samples, maximum):
        return sum(1 for sample in samples if sample >= maximum)

    # calculates total saturated sample count
    def count_total_saturation(self, samples, minimum, maximum):
        return (
            self.count_low_saturation(samples, minimum)
            + self.count_high_saturation(samples, maximum)
        )

    # calculates saturation percentage
    def calculate_saturation_percent(self, samples, minimum, maximum):
        saturated_count = self.count_total_saturation(
            samples,
            minimum,
            maximum,
        )

        return (saturated_count / len(samples)) * 100

    # analyzes saturation behavior
    def analyze(self, samples, minimum, maximum):
        low_count = self.count_low_saturation(samples, minimum)
        high_count = self.count_high_saturation(samples, maximum)
        total_count = low_count + high_count

        return {
            "analysis": "saturation",
            "sample_count": len(samples),
            "minimum": minimum,
            "maximum": maximum,
            "low_saturation_count": low_count,
            "high_saturation_count": high_count,
            "total_saturation_count": total_count,
            "saturation_percent": (total_count / len(samples)) * 100,
        }