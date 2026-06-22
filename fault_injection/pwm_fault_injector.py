# injects pwm timing and duty cycle faults


class PwmFaultInjector:
    # stores pwm fault injection settings
    def __init__(
        self,
        frequency_offset_hz=0,
        duty_cycle_offset_percent=0.0,
        jitter_us=0.0,
    ):
        self.frequency_offset_hz = frequency_offset_hz
        self.duty_cycle_offset_percent = duty_cycle_offset_percent
        self.jitter_us = jitter_us

    # injects a frequency offset
    def inject_frequency_fault(self, frequency_hz):
        return frequency_hz + self.frequency_offset_hz

    # injects a duty cycle offset
    def inject_duty_cycle_fault(self, duty_cycle_percent):
        faulted_duty_cycle = duty_cycle_percent + self.duty_cycle_offset_percent

        if faulted_duty_cycle < 0.0:
            return 0.0

        if faulted_duty_cycle > 100.0:
            return 100.0

        return faulted_duty_cycle

    # injects jitter into a period measurement
    def inject_jitter_fault(self, period_us):
        return period_us + self.jitter_us