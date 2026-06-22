# validates encoder position direction velocity and pulse loss


class EncoderValidator:
    # stores encoder validation limits
    def __init__(self, config):
        self.config = config

    # validates encoder position
    def validate_position(self, expected_counts, measured_counts):
        tolerance = self.config["position_tolerance_counts"]
        error = abs(expected_counts - measured_counts)

        return {
            "test": "encoder_position",
            "passed": error <= tolerance,
            "expected_counts": expected_counts,
            "measured_counts": measured_counts,
            "error_counts": error,
            "tolerance_counts": tolerance,
        }

    # validates encoder direction
    def validate_direction(self, measured_direction):
        expected_direction = self.config["expected_direction"]

        return {
            "test": "encoder_direction",
            "passed": measured_direction == expected_direction,
            "expected_direction": expected_direction,
            "measured_direction": measured_direction,
        }

    # validates encoder velocity
    def validate_velocity(self, expected_rpm, measured_rpm):
        tolerance = self.config["velocity_tolerance_rpm"]
        error = abs(expected_rpm - measured_rpm)

        return {
            "test": "encoder_velocity",
            "passed": error <= tolerance,
            "expected_rpm": expected_rpm,
            "measured_rpm": measured_rpm,
            "error_rpm": error,
            "tolerance_rpm": tolerance,
        }

    # validates encoder pulse loss
    def validate_pulse_loss(self, expected_pulses, measured_pulses):
        pulse_loss_limit = self.config["pulse_loss_limit"]
        lost_pulses = expected_pulses - measured_pulses

        if lost_pulses < 0:
            lost_pulses = 0

        return {
            "test": "encoder_pulse_loss",
            "passed": lost_pulses <= pulse_loss_limit,
            "expected_pulses": expected_pulses,
            "measured_pulses": measured_pulses,
            "lost_pulses": lost_pulses,
            "pulse_loss_limit": pulse_loss_limit,
        }