# tests pwm validation behavior

from validators.pwm_validator import PwmValidator


# creates a reusable pwm validator
def make_validator():
    config = {
        "frequency_tolerance_hz": 5,
        "duty_cycle_tolerance_percent": 1.0,
        "jitter_limit_us": 10,
        "enabled": True,
    }

    return PwmValidator(config)


# verifies frequency validation passes
def test_pwm_frequency_passes():
    validator = make_validator()

    result = validator.validate_frequency(1000, 1003)

    assert result["passed"] is True


# verifies frequency validation fails
def test_pwm_frequency_fails():
    validator = make_validator()

    result = validator.validate_frequency(1000, 1010)

    assert result["passed"] is False


# verifies duty cycle validation passes
def test_pwm_duty_cycle_passes():
    validator = make_validator()

    result = validator.validate_duty_cycle(50.0, 50.5)

    assert result["passed"] is True


# verifies duty cycle validation fails
def test_pwm_duty_cycle_fails():
    validator = make_validator()

    result = validator.validate_duty_cycle(50.0, 55.0)

    assert result["passed"] is False


# verifies jitter validation passes
def test_pwm_jitter_passes():
    validator = make_validator()

    result = validator.validate_jitter(5)

    assert result["passed"] is True


# verifies jitter validation fails
def test_pwm_jitter_fails():
    validator = make_validator()

    result = validator.validate_jitter(20)

    assert result["passed"] is False


# verifies enabled validation passes
def test_pwm_enabled_passes():
    validator = make_validator()

    result = validator.validate_enabled(True)

    assert result["passed"] is True


# verifies enabled validation fails
def test_pwm_enabled_fails():
    validator = make_validator()

    result = validator.validate_enabled(False)

    assert result["passed"] is False