# tests adapters and validators working together

from adapters.fake_adc_adapter import FakeAdcAdapter
from adapters.fake_dac_adapter import FakeDacAdapter
from adapters.fake_encoder_adapter import FakeEncoderAdapter
from adapters.fake_gpio_adapter import FakeGpioAdapter
from adapters.fake_pwm_adapter import FakePwmAdapter
from configs.config_loader import (
    load_adc_config,
    load_dac_config,
    load_encoder_config,
    load_gpio_config,
    load_pwm_config,
)
from validators.adc_validator import AdcValidator
from validators.dac_validator import DacValidator
from validators.encoder_validator import EncoderValidator
from validators.gpio_validator import GpioValidator
from validators.pwm_validator import PwmValidator


# verifies adc adapter output can be validated
def test_adc_adapter_validator_integration():
    config = load_adc_config()
    adc = FakeAdcAdapter(
        resolution_bits=config["resolution_bits"],
        reference_voltage=config["reference_voltage"],
        input_voltage=1.65,
        noise_volts=0.0,
    )
    validator = AdcValidator(config)

    measured_voltage = adc.read_voltage()
    result = validator.validate_accuracy(1.65, measured_voltage)

    assert result["passed"] is True


# verifies dac adapter output can be validated
def test_dac_adapter_validator_integration():
    config = load_dac_config()
    dac = FakeDacAdapter(
        resolution_bits=config["resolution_bits"],
        reference_voltage=config["reference_voltage"],
    )
    validator = DacValidator(config)

    dac.write_voltage(1.65)
    measured_voltage = dac.read_output_voltage()
    result = validator.validate_output(1.65, measured_voltage)

    assert result["passed"] is True


# verifies pwm adapter output can be validated
def test_pwm_adapter_validator_integration():
    config = load_pwm_config()
    pwm = FakePwmAdapter(
        frequency_hz=config["frequency_hz"],
        duty_cycle_percent=config["duty_cycle_percent"],
        jitter_us=0.0,
        enabled=True,
    )
    validator = PwmValidator(config)

    frequency_result = validator.validate_frequency(
        config["frequency_hz"],
        pwm.measure_frequency_hz(),
    )

    duty_cycle_result = validator.validate_duty_cycle(
        config["duty_cycle_percent"],
        pwm.measure_duty_cycle_percent(),
    )

    assert frequency_result["passed"] is True
    assert duty_cycle_result["passed"] is True


# verifies encoder adapter output can be validated
def test_encoder_adapter_validator_integration():
    config = load_encoder_config()
    encoder = FakeEncoderAdapter(
        pulses_per_revolution=config["pulses_per_revolution"],
        position_counts=1000,
        direction=config["expected_direction"],
        velocity_rpm=120,
    )
    validator = EncoderValidator(config)

    position_result = validator.validate_position(
        1000,
        encoder.read_position_counts(),
    )

    direction_result = validator.validate_direction(
        encoder.read_direction(),
    )

    assert position_result["passed"] is True
    assert direction_result["passed"] is True


# verifies gpio adapter output can be validated
def test_gpio_adapter_validator_integration():
    config = load_gpio_config()
    gpio = FakeGpioAdapter(
        mode=config["mode"],
        state="low",
        pull=config["pull"],
        interrupt_edge=config["interrupt_edge"],
    )
    validator = GpioValidator(config)

    gpio.write_state("high")
    result = validator.validate_state(
        "high",
        gpio.read_state(),
    )

    assert result["passed"] is True