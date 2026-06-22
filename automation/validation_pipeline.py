# runs hardware interface validation checks for supported interfaces

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


# checks whether one pipeline result passed
def pipeline_passed(results):
    return all(
        value is True
        for key, value in results.items()
        if key != "interface"
    )


# runs adc validation pipeline
def run_adc_pipeline():
    validator = AdcValidator(load_adc_config())

    return {
        "interface": "adc",
        "accuracy_valid": validator.validate_accuracy(1.65, 1.66)["passed"],
        "range_valid": validator.validate_range(1.65)["passed"],
        "saturation_valid": validator.validate_saturation(2048)["passed"],
        "noise_valid": validator.validate_noise([1.65, 1.651, 1.649])["passed"],
        "drift_valid": validator.validate_drift([1.65, 1.66])["passed"],
        "calibration_valid": validator.validate_calibration()["passed"],
    }


# runs dac validation pipeline
def run_dac_pipeline():
    validator = DacValidator(load_dac_config())

    return {
        "interface": "dac",
        "output_valid": validator.validate_output(1.65, 1.66)["passed"],
        "range_valid": validator.validate_range(1.65)["passed"],
        "linearity_valid": validator.validate_linearity(2.0, 2.01)["passed"],
        "settling_valid": validator.validate_settling_time(1.0)["passed"],
        "calibration_valid": validator.validate_calibration()["passed"],
    }


# runs pwm validation pipeline
def run_pwm_pipeline():
    validator = PwmValidator(load_pwm_config())

    return {
        "interface": "pwm",
        "frequency_valid": validator.validate_frequency(1000, 1003)["passed"],
        "duty_cycle_valid": validator.validate_duty_cycle(50.0, 50.5)["passed"],
        "jitter_valid": validator.validate_jitter(5)["passed"],
        "enabled_valid": validator.validate_enabled(True)["passed"],
    }


# runs encoder validation pipeline
def run_encoder_pipeline():
    validator = EncoderValidator(load_encoder_config())

    return {
        "interface": "encoder",
        "position_valid": validator.validate_position(1000, 1001)["passed"],
        "direction_valid": validator.validate_direction("forward")["passed"],
        "velocity_valid": validator.validate_velocity(120, 123)["passed"],
        "pulse_loss_valid": validator.validate_pulse_loss(1000, 1000)["passed"],
    }


# runs gpio validation pipeline
def run_gpio_pipeline():
    validator = GpioValidator(load_gpio_config())

    return {
        "interface": "gpio",
        "state_valid": validator.validate_state("high", "high")["passed"],
        "mode_valid": validator.validate_mode("output", "output")["passed"],
        "interrupt_valid": validator.validate_interrupt(True, True)["passed"],
        "debounce_valid": validator.validate_debounce_time(10)["passed"],
        "latency_valid": validator.validate_latency(3)["passed"],
        "glitch_valid": validator.validate_glitch(1)["passed"],
    }


# runs all hardware interface validation pipelines
def run_all_pipelines():
    pipelines = [
        run_adc_pipeline(),
        run_dac_pipeline(),
        run_pwm_pipeline(),
        run_encoder_pipeline(),
        run_gpio_pipeline(),
    ]

    return {
        "pipelines": pipelines,
        "status": "PASS" if all(pipeline_passed(item) for item in pipelines) else "FAIL",
    }


# starts validation pipeline from command line
def main():
    results = run_all_pipelines()

    print(results)


if __name__ == "__main__":
    main()