# injects encoder pulse loss direction and position faults


class EncoderFaultInjector:
    # stores encoder fault injection settings
    def __init__(
        self,
        lost_pulses=0,
        position_offset_counts=0,
        force_direction=None,
    ):
        self.lost_pulses = lost_pulses
        self.position_offset_counts = position_offset_counts
        self.force_direction = force_direction

    # injects pulse loss into measured pulses
    def inject_pulse_loss(self, measured_pulses):
        faulted_pulses = measured_pulses - self.lost_pulses

        if faulted_pulses < 0:
            return 0

        return faulted_pulses

    # injects a position offset
    def inject_position_fault(self, position_counts):
        return position_counts + self.position_offset_counts

    # injects a direction fault
    def inject_direction_fault(self, direction):
        if self.force_direction is None:
            return direction

        return self.force_direction