# tests pwm fault injection behavior

from fault_injection.pwm_fault_injector import PwmFaultInjector


# verifies frequency fault injection
def test_pwm_frequency_fault():
    injector = PwmFaultInjector(frequency_offset_hz=50)

    result = injector.inject_frequency_fault(1000)

    assert result == 1050


# verifies duty cycle fault injection
def test_pwm_duty_cycle_fault():
    injector = PwmFaultInjector(duty_cycle_offset_percent=10.0)

    result = injector.inject_duty_cycle_fault(50.0)

    assert result == 60.0


# verifies low duty cycle is clamped
def test_pwm_low_duty_cycle_fault_clamp():
    injector = PwmFaultInjector(duty_cycle_offset_percent=-80.0)

    result = injector.inject_duty_cycle_fault(50.0)

    assert result == 0.0


# verifies high duty cycle is clamped
def test_pwm_high_duty_cycle_fault_clamp():
    injector = PwmFaultInjector(duty_cycle_offset_percent=80.0)

    result = injector.inject_duty_cycle_fault(50.0)

    assert result == 100.0


# verifies jitter fault injection
def test_pwm_jitter_fault():
    injector = PwmFaultInjector(jitter_us=5.0)

    result = injector.inject_jitter_fault(1000.0)

    assert result == 1005.0