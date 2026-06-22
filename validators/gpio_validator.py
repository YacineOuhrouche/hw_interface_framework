# validates gpio state interrupt debounce latency and glitches


class GpioValidator:
    # stores gpio validation limits
    def __init__(self, config):
        self.config = config

    # validates gpio state
    def validate_state(self, expected_state, measured_state):
        return {
            "test": "gpio_state",
            "passed": measured_state == expected_state,
            "expected_state": expected_state,
            "measured_state": measured_state,
        }

    # validates gpio mode
    def validate_mode(self, expected_mode, measured_mode):
        return {
            "test": "gpio_mode",
            "passed": measured_mode == expected_mode,
            "expected_mode": expected_mode,
            "measured_mode": measured_mode,
        }

    # validates interrupt trigger state
    def validate_interrupt(self, expected_triggered, measured_triggered):
        return {
            "test": "gpio_interrupt",
            "passed": measured_triggered == expected_triggered,
            "expected_triggered": expected_triggered,
            "measured_triggered": measured_triggered,
        }

    # validates debounce time
    def validate_debounce_time(self, measured_debounce_ms):
        limit = self.config["debounce_time_ms"]

        return {
            "test": "gpio_debounce",
            "passed": measured_debounce_ms >= limit,
            "measured_debounce_ms": measured_debounce_ms,
            "limit_ms": limit,
        }

    # validates gpio latency
    def validate_latency(self, measured_latency_ms):
        limit = self.config["latency_limit_ms"]

        return {
            "test": "gpio_latency",
            "passed": measured_latency_ms <= limit,
            "measured_latency_ms": measured_latency_ms,
            "limit_ms": limit,
        }

    # validates gpio glitch duration
    def validate_glitch(self, glitch_duration_ms):
        limit = self.config["glitch_limit_ms"]

        return {
            "test": "gpio_glitch",
            "passed": glitch_duration_ms <= limit,
            "glitch_duration_ms": glitch_duration_ms,
            "limit_ms": limit,
        }