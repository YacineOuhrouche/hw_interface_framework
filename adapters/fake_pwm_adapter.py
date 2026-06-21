# simulates a pwm interface for validation without real hardware

import random

from adapters.base_interface_adapter import BaseInterfaceAdapter


class FakePwmAdapter(BaseInterfaceAdapter):
    # stores pwm configuration and output state
    def __init__(
        self,
        name="fake_pwm",
        frequency_hz=1000,
        duty_cycle_percent=50.0,
        jitter_us=0.0,
        enabled=False,
    ):
        super().__init__(name)
        self.frequency_hz = frequency_hz
        self.duty_cycle_percent = duty_cycle_percent
        self.jitter_us = jitter_us
        self.enabled = enabled

    # enables the simulated pwm output
    def enable(self):
        self.enabled = True

    # disables the simulated pwm output
    def disable(self):
        self.enabled = False

    # updates the simulated pwm frequency
    def set_frequency(self, frequency_hz):
        self.frequency_hz = frequency_hz

    # updates the simulated pwm duty cycle
    def set_duty_cycle(self, duty_cycle_percent):
        if duty_cycle_percent < 0.0:
            self.duty_cycle_percent = 0.0
        elif duty_cycle_percent > 100.0:
            self.duty_cycle_percent = 100.0
        else:
            self.duty_cycle_percent = duty_cycle_percent

    # updates the simulated pwm jitter
    def set_jitter(self, jitter_us):
        self.jitter_us = jitter_us

    # returns the pwm period in microseconds
    def get_period_us(self):
        return 1_000_000 / self.frequency_hz

    # returns the pwm high time in microseconds
    def get_high_time_us(self):
        return self.get_period_us() * (self.duty_cycle_percent / 100.0)

    # returns the pwm low time in microseconds
    def get_low_time_us(self):
        return self.get_period_us() - self.get_high_time_us()

    # returns a simulated measured period with jitter
    def measure_period_us(self):
        jitter = random.uniform(-self.jitter_us, self.jitter_us)

        return self.get_period_us() + jitter

    # returns a simulated measured frequency with jitter
    def measure_frequency_hz(self):
        measured_period = self.measure_period_us()

        return 1_000_000 / measured_period

    # returns a simulated measured duty cycle
    def measure_duty_cycle_percent(self):
        return self.duty_cycle_percent

    # returns the current pwm state
    def get_state(self):
        return {
            "name": self.name,
            "enabled": self.enabled,
            "frequency_hz": self.frequency_hz,
            "duty_cycle_percent": self.duty_cycle_percent,
            "jitter_us": self.jitter_us,
        }