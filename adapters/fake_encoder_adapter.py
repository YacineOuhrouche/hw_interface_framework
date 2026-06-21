# simulates an encoder interface for validation without real hardware


from adapters.base_interface_adapter import BaseInterfaceAdapter


class FakeEncoderAdapter(BaseInterfaceAdapter):
    # stores encoder configuration and motion state
    def __init__(
        self,
        name="fake_encoder",
        pulses_per_revolution=1024,
        position_counts=0,
        direction="forward",
        velocity_rpm=0.0,
    ):
        super().__init__(name)
        self.pulses_per_revolution = pulses_per_revolution
        self.position_counts = position_counts
        self.direction = direction
        self.velocity_rpm = velocity_rpm

    # updates the simulated encoder position
    def set_position_counts(self, position_counts):
        self.position_counts = position_counts

    # updates the simulated encoder direction
    def set_direction(self, direction):
        if direction not in ["forward", "reverse", "stopped"]:
            raise ValueError("direction must be forward, reverse, or stopped")

        self.direction = direction

    # updates the simulated encoder velocity
    def set_velocity_rpm(self, velocity_rpm):
        self.velocity_rpm = velocity_rpm

    # advances the encoder by a number of counts
    def step_counts(self, counts):
        if self.direction == "forward":
            self.position_counts += counts
        elif self.direction == "reverse":
            self.position_counts -= counts

        return self.position_counts

    # converts encoder counts to revolutions
    def counts_to_revolutions(self, counts):
        return counts / self.pulses_per_revolution

    # converts revolutions to encoder counts
    def revolutions_to_counts(self, revolutions):
        return round(revolutions * self.pulses_per_revolution)

    # returns the current encoder position
    def read_position_counts(self):
        return self.position_counts

    # returns the current encoder direction
    def read_direction(self):
        return self.direction

    # returns the current encoder velocity
    def read_velocity_rpm(self):
        return self.velocity_rpm

    # returns the current encoder state
    def get_state(self):
        return {
            "name": self.name,
            "pulses_per_revolution": self.pulses_per_revolution,
            "position_counts": self.position_counts,
            "direction": self.direction,
            "velocity_rpm": self.velocity_rpm,
        }