# tests encoder validation behavior

from validators.encoder_validator import EncoderValidator


# creates a reusable encoder validator
def make_validator():
    config = {
        "expected_direction": "forward",
        "velocity_tolerance_rpm": 5,
        "position_tolerance_counts": 2,
        "pulse_loss_limit": 0,
    }

    return EncoderValidator(config)


# verifies position validation passes
def test_encoder_position_passes():
    validator = make_validator()

    result = validator.validate_position(1000, 1001)

    assert result["passed"] is True


# verifies position validation fails
def test_encoder_position_fails():
    validator = make_validator()

    result = validator.validate_position(1000, 1010)

    assert result["passed"] is False


# verifies direction validation passes
def test_encoder_direction_passes():
    validator = make_validator()

    result = validator.validate_direction("forward")

    assert result["passed"] is True


# verifies direction validation fails
def test_encoder_direction_fails():
    validator = make_validator()

    result = validator.validate_direction("reverse")

    assert result["passed"] is False


# verifies velocity validation passes
def test_encoder_velocity_passes():
    validator = make_validator()

    result = validator.validate_velocity(120, 123)

    assert result["passed"] is True


# verifies velocity validation fails
def test_encoder_velocity_fails():
    validator = make_validator()

    result = validator.validate_velocity(120, 140)

    assert result["passed"] is False


# verifies pulse loss validation passes
def test_encoder_pulse_loss_passes():
    validator = make_validator()

    result = validator.validate_pulse_loss(1000, 1000)

    assert result["passed"] is True


# verifies pulse loss validation fails
def test_encoder_pulse_loss_fails():
    validator = make_validator()

    result = validator.validate_pulse_loss(1000, 990)

    assert result["passed"] is False


# verifies extra pulses do not count as lost pulses
def test_encoder_extra_pulses_do_not_count_as_loss():
    validator = make_validator()

    result = validator.validate_pulse_loss(1000, 1010)

    assert result["lost_pulses"] == 0
    assert result["passed"] is True