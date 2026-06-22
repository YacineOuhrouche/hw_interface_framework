# tests gpio fault injection behavior

from fault_injection.gpio_fault_injector import GpioFaultInjector


# verifies state fault is unchanged when not forced
def test_gpio_state_fault_unchanged():
    injector = GpioFaultInjector()

    result = injector.inject_state_fault("low")

    assert result == "low"


# verifies forced state fault
def test_gpio_state_fault_forced():
    injector = GpioFaultInjector(force_state="high")

    result = injector.inject_state_fault("low")

    assert result == "high"


# verifies glitch is unchanged when not configured
def test_gpio_glitch_unchanged():
    injector = GpioFaultInjector()

    result = injector.inject_glitch("low")

    assert result == "low"


# verifies glitch state injection
def test_gpio_glitch_injected():
    injector = GpioFaultInjector(glitch_state="high")

    result = injector.inject_glitch("low")

    assert result == "high"


# verifies interrupt fault is unchanged when not forced
def test_gpio_interrupt_fault_unchanged():
    injector = GpioFaultInjector()

    result = injector.inject_interrupt_fault(False)

    assert result is False


# verifies interrupt fault can be forced
def test_gpio_interrupt_fault_forced():
    injector = GpioFaultInjector(force_interrupt=True)

    result = injector.inject_interrupt_fault(False)

    assert result is True