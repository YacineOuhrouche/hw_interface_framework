# simulates a dac interface for validation without real hardware

from adapters.base_interface_adapter import BaseInterfaceAdapter


class FakeDacAdapter(BaseInterfaceAdapter):
    # stores dac configuration and output state
    def __init__(
        self,
        name="fake_dac",
        resolution_bits=12,
        reference_voltage=3.3,
    ):
        super().__init__(name)
        self.resolution_bits = resolution_bits
        self.reference_voltage = reference_voltage
        self.output_code = 0
        self.output_voltage = 0.0

    # returns the maximum dac digital code
    def get_max_code(self):
        return (2**self.resolution_bits) - 1

    # clamps a voltage to the dac output range
    def clamp_voltage(self, voltage):
        if voltage < 0.0:
            return 0.0

        if voltage > self.reference_voltage:
            return self.reference_voltage

        return voltage

    # clamps a code to the dac code range
    def clamp_code(self, code):
        if code < 0:
            return 0

        if code > self.get_max_code():
            return self.get_max_code()

        return code

    # converts voltage to dac code
    def voltage_to_code(self, voltage):
        clamped_voltage = self.clamp_voltage(voltage)
        ratio = clamped_voltage / self.reference_voltage

        return round(ratio * self.get_max_code())

    # converts dac code to voltage
    def code_to_voltage(self, code):
        clamped_code = self.clamp_code(code)
        ratio = clamped_code / self.get_max_code()

        return ratio * self.reference_voltage

    # writes a dac code and updates the output voltage
    def write_code(self, code):
        self.output_code = self.clamp_code(code)
        self.output_voltage = self.code_to_voltage(self.output_code)

        return self.output_voltage

    # writes a dac voltage and updates the output code
    def write_voltage(self, voltage):
        self.output_voltage = self.clamp_voltage(voltage)
        self.output_code = self.voltage_to_code(self.output_voltage)

        return self.output_code

    # returns the current dac output voltage
    def read_output_voltage(self):
        return self.output_voltage

    # returns the current dac output code
    def read_output_code(self):
        return self.output_code