# injects gpio state glitches stuck states and interrupt faults


class GpioFaultInjector:
    # stores gpio fault injection settings
    def __init__(
        self,
        force_state=None,
        glitch_state=None,
        force_interrupt=None,
    ):
        self.force_state = force_state
        self.glitch_state = glitch_state
        self.force_interrupt = force_interrupt

    # injects a forced gpio state
    def inject_state_fault(self, state):
        if self.force_state is None:
            return state

        return self.force_state

    # injects a temporary gpio glitch state
    def inject_glitch(self, state):
        if self.glitch_state is None:
            return state

        return self.glitch_state

    # injects an interrupt fault
    def inject_interrupt_fault(self, interrupt_triggered):
        if self.force_interrupt is None:
            return interrupt_triggered

        return self.force_interrupt