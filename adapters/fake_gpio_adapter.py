# simulates a gpio interface for validation without real hardware


from adapters.base_interface_adapter import BaseInterfaceAdapter


class FakeGpioAdapter(BaseInterfaceAdapter):
    # stores gpio configuration and pin state
    def __init__(
        self,
        name="fake_gpio",
        mode="output",
        state="low",
        pull="none",
        interrupt_edge="rising",
    ):
        super().__init__(name)
        self.mode = mode
        self.state = state
        self.pull = pull
        self.interrupt_edge = interrupt_edge
        self.interrupt_triggered = False

    # updates the gpio mode
    def set_mode(self, mode):
        if mode not in ["input", "output"]:
            raise ValueError("mode must be input or output")

        self.mode = mode

    # updates the gpio pull configuration
    def set_pull(self, pull):
        if pull not in ["none", "pull_up", "pull_down"]:
            raise ValueError("pull must be none, pull_up, or pull_down")

        self.pull = pull

    # updates the interrupt edge
    def set_interrupt_edge(self, interrupt_edge):
        if interrupt_edge not in ["rising", "falling", "both", "none"]:
            raise ValueError("interrupt edge must be rising, falling, both, or none")

        self.interrupt_edge = interrupt_edge

    # writes the gpio output state
    def write_state(self, state):
        if self.mode != "output":
            raise RuntimeError("cannot write when gpio is not output")

        if state not in ["low", "high"]:
            raise ValueError("state must be low or high")

        self.state = state

    # reads the gpio state
    def read_state(self):
        return self.state

    # simulates an external input state
    def simulate_input_state(self, state):
        if self.mode != "input":
            raise RuntimeError("cannot simulate input when gpio is not input")

        if state not in ["low", "high"]:
            raise ValueError("state must be low or high")

        previous_state = self.state
        self.state = state
        self.check_interrupt(previous_state, state)

    # checks whether an interrupt should trigger
    def check_interrupt(self, previous_state, new_state):
        rising_edge = previous_state == "low" and new_state == "high"
        falling_edge = previous_state == "high" and new_state == "low"

        if self.interrupt_edge == "rising" and rising_edge:
            self.interrupt_triggered = True

        if self.interrupt_edge == "falling" and falling_edge:
            self.interrupt_triggered = True

        if self.interrupt_edge == "both" and (rising_edge or falling_edge):
            self.interrupt_triggered = True

    # clears the interrupt state
    def clear_interrupt(self):
        self.interrupt_triggered = False

    # returns true when interrupt was triggered
    def was_interrupt_triggered(self):
        return self.interrupt_triggered

    # returns the current gpio state
    def get_state(self):
        return {
            "name": self.name,
            "mode": self.mode,
            "state": self.state,
            "pull": self.pull,
            "interrupt_edge": self.interrupt_edge,
            "interrupt_triggered": self.interrupt_triggered,
        }