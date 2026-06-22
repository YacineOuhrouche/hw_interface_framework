# tests adc validation behavior

from validators.adc_validator import AdcValidator


# creates a reusable adc validator
def make_validator():
    config = {
        "input_min_voltage": 0.0,
        "input_max_voltage": 3.3,
        "accuracy_tolerance_volts": 0.02,
        "noise_limit_volts": 0.01,
        "drift_limit_volts": 0.02,
        "saturation_min_code": 0,
        "saturation_max_code": 4095,
        "calibration_offset_volts": 0.0,
        "calibration_gain": 1.0,
    }

    return AdcValidator(config)


# verifies that adc accuracy passes inside tolerance
def test_adc_accuracy_passes():
    validator = make_validator()

    result = validator.validate_accuracy(1.65, 1.66)

    assert result["passed"] is True


# verifies that adc accuracy fails outside tolerance
def test_adc_accuracy_fails():
    validator = make_validator()

    result = validator.validate_accuracy(1.65, 1.70)

    assert result["passed"] is False


# verifies that adc range passes inside range
def test_adc_range_passes():
    validator = make_validator()

    result = validator.validate_range(1.65)

    assert result["passed"] is True


# verifies that adc range fails below range
def test_adc_range_fails_low():
    validator = make_validator()

    result = validator.validate_range(-0.1)

    assert result["passed"] is False


# verifies that adc range fails above range
def test_adc_range_fails_high():
    validator = make_validator()

    result = validator.validate_range(3.5)

    assert result["passed"] is False


# verifies that adc saturation passes when code is not saturated
def test_adc_saturation_passes():
    validator = make_validator()

    result = validator.validate_saturation(2048)

    assert result["passed"] is True


# verifies that adc saturation fails at minimum code
def test_adc_saturation_fails_minimum():
    validator = make_validator()

    result = validator.validate_saturation(0)

    assert result["passed"] is False


# verifies that adc saturation fails at maximum code
def test_adc_saturation_fails_maximum():
    validator = make_validator()

    result = validator.validate_saturation(4095)

    assert result["passed"] is False


# verifies that adc noise passes inside limit
def test_adc_noise_passes():
    validator = make_validator()
    samples = [1.65, 1.651, 1.649, 1.652, 1.648]

    result = validator.validate_noise(samples)

    assert result["passed"] is True


# verifies that adc noise fails outside limit
def test_adc_noise_fails():
    validator = make_validator()
    samples = [1.65, 1.67, 1.63, 1.66, 1.64]

    result = validator.validate_noise(samples)

    assert result["passed"] is False


# verifies that adc drift passes inside limit
def test_adc_drift_passes():
    validator = make_validator()
    samples = [1.65, 1.655, 1.66]

    result = validator.validate_drift(samples)

    assert result["passed"] is True


# verifies that adc drift fails outside limit
def test_adc_drift_fails():
    validator = make_validator()
    samples = [1.65, 1.68]

    result = validator.validate_drift(samples)

    assert result["passed"] is False


# verifies that adc calibration passes
def test_adc_calibration_passes():
    validator = make_validator()

    result = validator.validate_calibration()

    assert result["passed"] is True