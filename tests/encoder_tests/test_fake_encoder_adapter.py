# tests the fake encoder adapter behavior

import pytest

from adapters.fake_encoder_adapter import FakeEncoderAdapter


# verifies that the fake encoder starts with the expected configuration
def test_fake_encoder_configuration():
    encoder = FakeEncoderAdapter(
        pulses_per_revolution=1024,
        position_counts=0,
        direction="forward",
        velocity_rpm=120.0,
    )

    assert encoder.pulses_per_revolution == 1024
    assert encoder.position_counts == 0
    assert encoder.direction == "forward"
    assert encoder.velocity_rpm == 120.0


# verifies that the encoder position can be updated
def test_fake_encoder_set_position():
    encoder = FakeEncoderAdapter()

    encoder.set_position_counts(500)

    assert encoder.read_position_counts() == 500


# verifies that the encoder direction can be updated
def test_fake_encoder_set_direction():
    encoder = FakeEncoderAdapter()

    encoder.set_direction("reverse")

    assert encoder.read_direction() == "reverse"


# verifies that invalid direction raises an error
def test_fake_encoder_invalid_direction():
    encoder = FakeEncoderAdapter()

    with pytest.raises(ValueError):
        encoder.set_direction("sideways")


# verifies that the encoder velocity can be updated
def test_fake_encoder_set_velocity():
    encoder = FakeEncoderAdapter()

    encoder.set_velocity_rpm(250.0)

    assert encoder.read_velocity_rpm() == 250.0


# verifies that forward stepping increases position
def test_fake_encoder_forward_step():
    encoder = FakeEncoderAdapter(direction="forward")

    position = encoder.step_counts(100)

    assert position == 100


# verifies that reverse stepping decreases position
def test_fake_encoder_reverse_step():
    encoder = FakeEncoderAdapter(direction="reverse")

    position = encoder.step_counts(100)

    assert position == -100


# verifies that stopped stepping does not change position
def test_fake_encoder_stopped_step():
    encoder = FakeEncoderAdapter(direction="stopped")

    position = encoder.step_counts(100)

    assert position == 0


# verifies that counts convert to revolutions
def test_fake_encoder_counts_to_revolutions():
    encoder = FakeEncoderAdapter(pulses_per_revolution=1000)

    revolutions = encoder.counts_to_revolutions(500)

    assert revolutions == 0.5


# verifies that revolutions convert to counts
def test_fake_encoder_revolutions_to_counts():
    encoder = FakeEncoderAdapter(pulses_per_revolution=1000)

    counts = encoder.revolutions_to_counts(2.5)

    assert counts == 2500


# verifies that encoder state is returned
def test_fake_encoder_state():
    encoder = FakeEncoderAdapter(
        pulses_per_revolution=1024,
        position_counts=10,
        direction="forward",
        velocity_rpm=50.0,
    )

    state = encoder.get_state()

    assert state["pulses_per_revolution"] == 1024
    assert state["position_counts"] == 10
    assert state["direction"] == "forward"
    assert state["velocity_rpm"] == 50.0