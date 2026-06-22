# tests encoder fault injection behavior

from fault_injection.encoder_fault_injector import EncoderFaultInjector


# verifies pulse loss injection
def test_encoder_pulse_loss():
    injector = EncoderFaultInjector(lost_pulses=10)

    result = injector.inject_pulse_loss(100)

    assert result == 90


# verifies pulse loss does not go below zero
def test_encoder_pulse_loss_clamps_to_zero():
    injector = EncoderFaultInjector(lost_pulses=200)

    result = injector.inject_pulse_loss(100)

    assert result == 0


# verifies position fault injection
def test_encoder_position_fault():
    injector = EncoderFaultInjector(position_offset_counts=25)

    result = injector.inject_position_fault(100)

    assert result == 125


# verifies direction fault is unchanged when not forced
def test_encoder_direction_fault_unchanged():
    injector = EncoderFaultInjector()

    result = injector.inject_direction_fault("forward")

    assert result == "forward"


# verifies direction fault can be forced
def test_encoder_direction_fault_forced():
    injector = EncoderFaultInjector(force_direction="reverse")

    result = injector.inject_direction_fault("forward")

    assert result == "reverse"