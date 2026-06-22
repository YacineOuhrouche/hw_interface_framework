# injects adc saturation into voltage samples


class AdcSaturationInjector:
    # stores adc saturation injection settings
    def __init__(
        self,
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    ):
        self.minimum_voltage = minimum_voltage
        self.maximum_voltage = maximum_voltage

    # forces one sample to low saturation
    def inject_low_saturation(self):
        return self.minimum_voltage

    # forces one sample to high saturation
    def inject_high_saturation(self):
        return self.maximum_voltage

    # clamps one sample into saturation limits
    def clamp_sample(self, sample):
        if sample < self.minimum_voltage:
            return self.minimum_voltage

        if sample > self.maximum_voltage:
            return self.maximum_voltage

        return sample

    # clamps multiple samples into saturation limits
    def clamp_samples(self, samples):
        clamped_samples = []

        for sample in samples:
            clamped_samples.append(self.clamp_sample(sample))

        return clamped_samples