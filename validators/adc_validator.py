# validates adc measurements for accuracy range saturation noise drift and calibration

import statistics


class AdcValidator:
    # stores adc validation limits
    def __init__(self, config):
        self.config = config

    # validates that measured voltage is close to expected voltage
    def validate_accuracy(self, expected_voltage, measured_voltage):
        tolerance = self.config["accuracy_tolerance_volts"]
        error = abs(expected_voltage - measured_voltage)

        return {
            "test": "adc_accuracy",
            "passed": error <= tolerance,
            "expected_voltage": expected_voltage,
            "measured_voltage": measured_voltage,
            "error_volts": error,
            "tolerance_volts": tolerance,
        }

    # validates that measured voltage is inside the allowed input range
    def validate_range(self, measured_voltage):
        minimum = self.config["input_min_voltage"]
        maximum = self.config["input_max_voltage"]

        return {
            "test": "adc_range",
            "passed": minimum <= measured_voltage <= maximum,
            "measured_voltage": measured_voltage,
            "minimum_voltage": minimum,
            "maximum_voltage": maximum,
        }

    # validates that adc code is not saturated
    def validate_saturation(self, code):
        minimum_code = self.config["saturation_min_code"]
        maximum_code = self.config["saturation_max_code"]
        saturated = code <= minimum_code or code >= maximum_code

        return {
            "test": "adc_saturation",
            "passed": not saturated,
            "code": code,
            "minimum_code": minimum_code,
            "maximum_code": maximum_code,
            "saturated": saturated,
        }

    # validates that sample noise is within the allowed limit
    def validate_noise(self, samples):
        noise_limit = self.config["noise_limit_volts"]
        mean_voltage = statistics.mean(samples)
        peak_noise = max(abs(sample - mean_voltage) for sample in samples)

        return {
            "test": "adc_noise",
            "passed": peak_noise <= noise_limit,
            "mean_voltage": mean_voltage,
            "peak_noise_volts": peak_noise,
            "noise_limit_volts": noise_limit,
            "sample_count": len(samples),
        }

    # validates that sample drift is within the allowed limit
    def validate_drift(self, samples):
        drift_limit = self.config["drift_limit_volts"]
        drift = abs(samples[-1] - samples[0])

        return {
            "test": "adc_drift",
            "passed": drift <= drift_limit,
            "start_voltage": samples[0],
            "end_voltage": samples[-1],
            "drift_volts": drift,
            "drift_limit_volts": drift_limit,
        }

    # validates calibration gain and offset
    def validate_calibration(self):
        offset = self.config["calibration_offset_volts"]
        gain = self.config["calibration_gain"]
        offset_valid = abs(offset) <= self.config["accuracy_tolerance_volts"]
        gain_valid = abs(gain - 1.0) <= 0.05

        return {
            "test": "adc_calibration",
            "passed": offset_valid and gain_valid,
            "calibration_offset_volts": offset,
            "calibration_gain": gain,
            "offset_valid": offset_valid,
            "gain_valid": gain_valid,
        }