# tests adc noise injection behavior

from fault_injection.adc_noise_injector import AdcNoiseInjector


# verifies that noise injection keeps sample inside expected bounds
def test_adc_noise_inject_sample_bounds():
    injector = AdcNoiseInjector(noise_amplitude_volts=0.01)

    result = injector.inject_sample(1.65)

    assert 1.64 <= result <= 1.66


# verifies that noise injection returns the same number of samples
def test_adc_noise_inject_samples_count():
    injector = AdcNoiseInjector(noise_amplitude_volts=0.01)
    samples = [1.65, 1.65, 1.65]

    result = injector.inject_samples(samples)

    assert len(result) == 3


# verifies that noise amplitude can be updated
def test_adc_noise_amplitude_update():
    injector = AdcNoiseInjector(noise_amplitude_volts=0.01)

    injector.set_noise_amplitude(0.05)

    assert injector.noise_amplitude_volts == 0.05