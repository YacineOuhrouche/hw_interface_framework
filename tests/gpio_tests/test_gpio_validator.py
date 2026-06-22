# tests gpio validation behavior

from validators.gpio_validator import GpioValidator


# creates a reusable gpio validator
def make_validator():
    config = {
        "debounce_time_ms": 10,
        "latency_limit_ms": 5,
        "glitch_limit_ms": 2,
    }

    return GpioValidator(config)


# verifies gpio state validation passes
def test_gpio_state_passes():
    validator = make_validator()

    result = validator.validate_state("high", "high")

    assert result["passed"] is True


# verifies gpio state validation fails
def test_gpio_state_fails():
    validator = make_validator()

    result = validator.validate_state("high", "low")

    assert result["passed"] is False


# verifies gpio mode validation passes
def test_gpio_mode_passes():
    validator = make_validator()

    result = validator.validate_mode("output", "output")

    assert result["passed"] is True


# verifies gpio mode validation fails
def test_gpio_mode_fails():
    validator = make_validator()

    result = validator.validate_mode("output", "input")

    assert result["passed"] is False


# verifies gpio interrupt validation passes
def test_gpio_interrupt_passes():
    validator = make_validator()

    result = validator.validate_interrupt(True, True)

    assert result["passed"] is True


# verifies gpio interrupt validation fails
def test_gpio_interrupt_fails():
    validator = make_validator()

    result = validator.validate_interrupt(True, False)

    assert result["passed"] is False


# verifies debounce validation passes
def test_gpio_debounce_passes():
    validator = make_validator()

    result = validator.validate_debounce_time(10)

    assert result["passed"] is True


# verifies debounce validation fails
def test_gpio_debounce_fails():
    validator = make_validator()

    result = validator.validate_debounce_time(5)

    assert result["passed"] is False


# verifies latency validation passes
def test_gpio_latency_passes():
    validator = make_validator()

    result = validator.validate_latency(3)

    assert result["passed"] is True


# verifies latency validation fails
def test_gpio_latency_fails():
    validator = make_validator()

    result = validator.validate_latency(10)

    assert result["passed"] is False


# verifies glitch validation passes
def test_gpio_glitch_passes():
    validator = make_validator()

    result = validator.validate_glitch(1)

    assert result["passed"] is True


# verifies glitch validation fails
def test_gpio_glitch_fails():
    validator = make_validator()

    result = validator.validate_glitch(5)

    assert result["passed"] is False