# injects noise into adc sample data

import random


class AdcNoiseInjector:
    # stores adc noise injection settings
    def __init__(self, noise_amplitude_volts=0.01):
        self.noise_amplitude_volts = noise_amplitude_volts

    # injects noise into one sample
    def inject_sample(self, sample):
        noise = random.uniform(
            -self.noise_amplitude_volts,
            self.noise_amplitude_volts,
        )

        return sample + noise

    # injects noise into multiple samples
    def inject_samples(self, samples):
        noisy_samples = []

        for sample in samples:
            noisy_samples.append(self.inject_sample(sample))

        return noisy_samples

    # updates the noise amplitude
    def set_noise_amplitude(self, noise_amplitude_volts):
        self.noise_amplitude_volts = noise_amplitude_volts