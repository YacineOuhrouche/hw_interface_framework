# tests the fake pwm adapter behavior

from adapters.fake_pwm_adapter import FakePwmAdapter


# verifies that the fake pwm starts with the expected configuration
def test_fake_pwm_configuration():
    pwm = FakePwmAdapter(
        frequency_hz=1000,
        duty_cycle_percent=50.0,
    )

    assert pwm.frequency_hz == 1000
    assert pwm.duty_cycle_percent == 50.0
    assert pwm.enabled is False


# verifies that the fake pwm can be enabled
def test_fake_pwm_enable():
    pwm = FakePwmAdapter()

    pwm.enable()

    assert pwm.enabled is True


# verifies that the fake pwm can be disabled
def test_fake_pwm_disable():
    pwm = FakePwmAdapter(enabled=True)

    pwm.disable()

    assert pwm.enabled is False


# verifies that the fake pwm frequency can be updated
def test_fake_pwm_set_frequency():
    pwm = FakePwmAdapter()

    pwm.set_frequency(2000)

    assert pwm.frequency_hz == 2000


# verifies that the fake pwm duty cycle can be updated
def test_fake_pwm_set_duty_cycle():
    pwm = FakePwmAdapter()

    pwm.set_duty_cycle(25.0)

    assert pwm.duty_cycle_percent == 25.0


# verifies that low duty cycle is clamped
def test_fake_pwm_low_duty_cycle_clamp():
    pwm = FakePwmAdapter()

    pwm.set_duty_cycle(-10.0)

    assert pwm.duty_cycle_percent == 0.0


# verifies that high duty cycle is clamped
def test_fake_pwm_high_duty_cycle_clamp():
    pwm = FakePwmAdapter()

    pwm.set_duty_cycle(120.0)

    assert pwm.duty_cycle_percent == 100.0


# verifies that the pwm period is calculated
def test_fake_pwm_period():
    pwm = FakePwmAdapter(frequency_hz=1000)

    assert pwm.get_period_us() == 1000.0


# verifies that the pwm high time is calculated
def test_fake_pwm_high_time():
    pwm = FakePwmAdapter(frequency_hz=1000, duty_cycle_percent=25.0)

    assert pwm.get_high_time_us() == 250.0


# verifies that the pwm low time is calculated
def test_fake_pwm_low_time():
    pwm = FakePwmAdapter(frequency_hz=1000, duty_cycle_percent=25.0)

    assert pwm.get_low_time_us() == 750.0


# verifies that measured frequency is close to the configured frequency
def test_fake_pwm_measure_frequency():
    pwm = FakePwmAdapter(frequency_hz=1000, jitter_us=0.0)

    frequency = pwm.measure_frequency_hz()

    assert frequency == 1000.0


# verifies that measured duty cycle matches the configured duty cycle
def test_fake_pwm_measure_duty_cycle():
    pwm = FakePwmAdapter(duty_cycle_percent=60.0)

    duty_cycle = pwm.measure_duty_cycle_percent()

    assert duty_cycle == 60.0