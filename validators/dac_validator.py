# validates dac output range linearity settling and accuracy


class DacValidator:
    # stores dac validation limits
    def __init__(self, config):
        self.config = config

    # validates output voltage accuracy
    def validate_output(
        self,
        expected_voltage,
        measured_voltage,
    ):
        tolerance = self.config["output_tolerance_volts"]
        error = abs(expected_voltage - measured_voltage)

        return {
            "test": "dac_output",
            "passed": error <= tolerance,
            "expected_voltage": expected_voltage,
            "measured_voltage": measured_voltage,
            "error_volts": error,
            "tolerance_volts": tolerance,
        }

    # validates output voltage range
    def validate_range(self, measured_voltage):
        minimum = self.config["output_min_voltage"]
        maximum = self.config["output_max_voltage"]

        return {
            "test": "dac_range",
            "passed": minimum <= measured_voltage <= maximum,
            "measured_voltage": measured_voltage,
            "minimum_voltage": minimum,
            "maximum_voltage": maximum,
        }

    # validates linearity error
    def validate_linearity(
        self,
        expected_voltage,
        measured_voltage,
    ):
        tolerance = self.config["linearity_tolerance_volts"]
        error = abs(expected_voltage - measured_voltage)

        return {
            "test": "dac_linearity",
            "passed": error <= tolerance,
            "error_volts": error,
            "tolerance_volts": tolerance,
        }

    # validates settling time
    def validate_settling_time(
        self,
        settling_time_ms,
    ):
        limit = self.config["settling_time_limit_ms"]

        return {
            "test": "dac_settling_time",
            "passed": settling_time_ms <= limit,
            "settling_time_ms": settling_time_ms,
            "limit_ms": limit,
        }

    # validates calibration gain and offset
    def validate_calibration(self):
        offset = self.config["calibration_offset_volts"]
        gain = self.config["calibration_gain"]

        offset_valid = (
            abs(offset)
            <= self.config["output_tolerance_volts"]
        )

        gain_valid = abs(gain - 1.0) <= 0.05

        return {
            "test": "dac_calibration",
            "passed": offset_valid and gain_valid,
            "offset_valid": offset_valid,
            "gain_valid": gain_valid,
            "calibration_offset_volts": offset,
            "calibration_gain": gain,
        }