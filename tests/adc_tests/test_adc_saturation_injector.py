# tests adc saturation injection behavior

from fault_injection.adc_saturation_injector import AdcSaturationInjector


# verifies low saturation injection
def test_adc_low_saturation_injection():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.inject_low_saturation()

    assert result == 0.0


# verifies high saturation injection
def test_adc_high_saturation_injection():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.inject_high_saturation()

    assert result == 3.3


# verifies low sample clamp
def test_adc_low_sample_clamp():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.clamp_sample(-1.0)

    assert result == 0.0


# verifies high sample clamp
def test_adc_high_sample_clamp():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.clamp_sample(5.0)

    assert result == 3.3


# verifies normal sample is unchanged
def test_adc_normal_sample_unchanged():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.clamp_sample(1.65)

    assert result == 1.65


# verifies multiple samples are clamped
def test_adc_clamp_samples():
    injector = AdcSaturationInjector(
        minimum_voltage=0.0,
        maximum_voltage=3.3,
    )

    result = injector.clamp_samples(
        [-1.0, 1.65, 5.0]
    )

    assert result == [0.0, 1.65, 3.3]