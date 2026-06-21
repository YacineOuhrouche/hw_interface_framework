# simulates an adc interface for validation without real hardware

import random

from adapters.base_interface_adapter import BaseInterfaceAdapter


class FakeAdcAdapter(BaseInterfaceAdapter):
    # stores adc configuration and default input state
    def __init__(
        self,
        name="fake_adc",
        resolution_bits=12,
        reference_voltage=3.3,
        input_voltage=1.65,
        noise_volts=0.0,
    ):
        super().__init__(name)
        self.resolution_bits = resolution_bits
        self.reference_voltage = reference_voltage
        self.input_voltage = input_voltage
        self.noise_volts = noise_volts

    # updates the simulated input voltage
    def set_input_voltage(self, voltage):
        self.input_voltage = voltage

    # updates the simulated noise level
    def set_noise_volts(self, noise_volts):
        self.noise_volts = noise_volts

    # returns the maximum adc digital code
    def get_max_code(self):
        return (2**self.resolution_bits) - 1

    # clamps a voltage to the adc input range
    def clamp_voltage(self, voltage):
        if voltage < 0.0:
            return 0.0

        if voltage > self.reference_voltage:
            return self.reference_voltage

        return voltage

    # converts voltage to adc code
    def voltage_to_code(self, voltage):
        clamped_voltage = self.clamp_voltage(voltage)
        ratio = clamped_voltage / self.reference_voltage

        return round(ratio * self.get_max_code())

    # converts adc code to voltage
    def code_to_voltage(self, code):
        ratio = code / self.get_max_code()

        return ratio * self.reference_voltage

    # reads one simulated adc code
    def read_code(self):
        noise = random.uniform(-self.noise_volts, self.noise_volts)
        measured_voltage = self.input_voltage + noise

        return self.voltage_to_code(measured_voltage)

    # reads one simulated adc voltage
    def read_voltage(self):
        code = self.read_code()

        return self.code_to_voltage(code)

    # reads multiple simulated adc voltages
    def read_samples(self, sample_count):
        samples = []

        for _ in range(sample_count):
            samples.append(self.read_voltage())

        return samples