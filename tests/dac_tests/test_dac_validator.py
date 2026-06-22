# tests dac validation behavior

from validators.dac_validator import DacValidator


# creates a reusable dac validator
def make_validator():
    config = {
        "output_min_voltage": 0.0,
        "output_max_voltage": 3.3,
        "output_tolerance_volts": 0.02,
        "linearity_tolerance_volts": 0.02,
        "settling_time_limit_ms": 2.0,
        "calibration_offset_volts": 0.0,
        "calibration_gain": 1.0,
    }

    return DacValidator(config)


# verifies output validation passes
def test_dac_output_passes():
    validator = make_validator()

    result = validator.validate_output(
        1.65,
        1.66,
    )

    assert result["passed"] is True


# verifies output validation fails
def test_dac_output_fails():
    validator = make_validator()

    result = validator.validate_output(
        1.65,
        1.70,
    )

    assert result["passed"] is False


# verifies range validation passes
def test_dac_range_passes():
    validator = make_validator()

    result = validator.validate_range(2.0)

    assert result["passed"] is True


# verifies range validation fails
def test_dac_range_fails():
    validator = make_validator()

    result = validator.validate_range(5.0)

    assert result["passed"] is False


# verifies linearity validation passes
def test_dac_linearity_passes():
    validator = make_validator()

    result = validator.validate_linearity(
        2.0,
        2.01,
    )

    assert result["passed"] is True


# verifies linearity validation fails
def test_dac_linearity_fails():
    validator = make_validator()

    result = validator.validate_linearity(
        2.0,
        2.1,
    )

    assert result["passed"] is False


# verifies settling time passes
def test_dac_settling_time_passes():
    validator = make_validator()

    result = validator.validate_settling_time(
        1.0
    )

    assert result["passed"] is True


# verifies settling time fails
def test_dac_settling_time_fails():
    validator = make_validator()

    result = validator.validate_settling_time(
        5.0
    )

    assert result["passed"] is False


# verifies calibration passes
def test_dac_calibration_passes():
    validator = make_validator()

    result = validator.validate_calibration()

    assert result["passed"] is True