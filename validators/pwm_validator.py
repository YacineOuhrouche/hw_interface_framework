# validates pwm frequency duty cycle jitter and output state


class PwmValidator:
    # stores pwm validation limits
    def __init__(self, config):
        self.config = config

    # validates pwm frequency
    def validate_frequency(self, expected_frequency_hz, measured_frequency_hz):
        tolerance = self.config["frequency_tolerance_hz"]
        error = abs(expected_frequency_hz - measured_frequency_hz)

        return {
            "test": "pwm_frequency",
            "passed": error <= tolerance,
            "expected_frequency_hz": expected_frequency_hz,
            "measured_frequency_hz": measured_frequency_hz,
            "error_hz": error,
            "tolerance_hz": tolerance,
        }

    # validates pwm duty cycle
    def validate_duty_cycle(self, expected_duty_cycle, measured_duty_cycle):
        tolerance = self.config["duty_cycle_tolerance_percent"]
        error = abs(expected_duty_cycle - measured_duty_cycle)

        return {
            "test": "pwm_duty_cycle",
            "passed": error <= tolerance,
            "expected_duty_cycle": expected_duty_cycle,
            "measured_duty_cycle": measured_duty_cycle,
            "error_percent": error,
            "tolerance_percent": tolerance,
        }

    # validates pwm jitter
    def validate_jitter(self, measured_jitter_us):
        limit = self.config["jitter_limit_us"]

        return {
            "test": "pwm_jitter",
            "passed": measured_jitter_us <= limit,
            "measured_jitter_us": measured_jitter_us,
            "limit_us": limit,
        }

    # validates pwm output enabled state
    def validate_enabled(self, enabled):
        expected_enabled = self.config["enabled"]

        return {
            "test": "pwm_enabled",
            "passed": enabled == expected_enabled,
            "expected_enabled": expected_enabled,
            "measured_enabled": enabled,
        }