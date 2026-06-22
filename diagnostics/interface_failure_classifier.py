# classifies hardware interface validation failures


class InterfaceFailureClassifier:
    # stores failure classification rules
    def __init__(self):
        self.failure_map = {
            "adc_accuracy": "measurement_accuracy_failure",
            "adc_noise": "signal_noise_failure",
            "adc_drift": "signal_drift_failure",
            "adc_saturation": "signal_saturation_failure",
            "dac_output": "output_accuracy_failure",
            "dac_linearity": "linearity_failure",
            "dac_settling_time": "settling_time_failure",
            "pwm_frequency": "timing_frequency_failure",
            "pwm_duty_cycle": "duty_cycle_failure",
            "pwm_jitter": "timing_jitter_failure",
            "encoder_position": "position_tracking_failure",
            "encoder_direction": "direction_detection_failure",
            "encoder_velocity": "speed_measurement_failure",
            "encoder_pulse_loss": "pulse_integrity_failure",
            "gpio_state": "digital_state_failure",
            "gpio_interrupt": "interrupt_failure",
            "gpio_debounce": "debounce_failure",
            "gpio_latency": "latency_failure",
            "gpio_glitch": "glitch_failure",
        }

    # classifies one validation result
    def classify_result(self, result):
        if result["passed"]:
            return "none"

        test_name = result["test"]

        return self.failure_map.get(
            test_name,
            "unknown_failure",
        )

    # classifies multiple validation results
    def classify_results(self, results):
        classifications = []

        for result in results:
            classifications.append(
                {
                    "test": result["test"],
                    "passed": result["passed"],
                    "failure_type": self.classify_result(result),
                }
            )

        return classifications

    # returns only failed classifications
    def get_failures(self, results):
        classifications = self.classify_results(results)

        return [
            classification
            for classification in classifications
            if classification["failure_type"] != "none"
        ]