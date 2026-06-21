# tests the fake gpio adapter behavior

import pytest

from adapters.fake_gpio_adapter import FakeGpioAdapter


# verifies that the fake gpio starts with the expected configuration
def test_fake_gpio_configuration():
    gpio = FakeGpioAdapter(
        mode="output",
        state="low",
        pull="none",
        interrupt_edge="rising",
    )

    assert gpio.mode == "output"
    assert gpio.state == "low"
    assert gpio.pull == "none"
    assert gpio.interrupt_edge == "rising"


# verifies that gpio mode can be updated
def test_fake_gpio_set_mode():
    gpio = FakeGpioAdapter()

    gpio.set_mode("input")

    assert gpio.mode == "input"


# verifies that invalid gpio mode raises an error
def test_fake_gpio_invalid_mode():
    gpio = FakeGpioAdapter()

    with pytest.raises(ValueError):
        gpio.set_mode("analog")


# verifies that gpio pull can be updated
def test_fake_gpio_set_pull():
    gpio = FakeGpioAdapter()

    gpio.set_pull("pull_up")

    assert gpio.pull == "pull_up"


# verifies that invalid gpio pull raises an error
def test_fake_gpio_invalid_pull():
    gpio = FakeGpioAdapter()

    with pytest.raises(ValueError):
        gpio.set_pull("floating")


# verifies that output state can be written
def test_fake_gpio_write_state():
    gpio = FakeGpioAdapter(mode="output")

    gpio.write_state("high")

    assert gpio.read_state() == "high"


# verifies that writing in input mode raises an error
def test_fake_gpio_write_in_input_mode():
    gpio = FakeGpioAdapter(mode="input")

    with pytest.raises(RuntimeError):
        gpio.write_state("high")


# verifies that input state can be simulated
def test_fake_gpio_simulate_input_state():
    gpio = FakeGpioAdapter(mode="input", state="low")

    gpio.simulate_input_state("high")

    assert gpio.read_state() == "high"


# verifies that simulating input in output mode raises an error
def test_fake_gpio_simulate_input_in_output_mode():
    gpio = FakeGpioAdapter(mode="output")

    with pytest.raises(RuntimeError):
        gpio.simulate_input_state("high")


# verifies that rising interrupt triggers
def test_fake_gpio_rising_interrupt():
    gpio = FakeGpioAdapter(mode="input", state="low", interrupt_edge="rising")

    gpio.simulate_input_state("high")

    assert gpio.was_interrupt_triggered() is True


# verifies that falling interrupt triggers
def test_fake_gpio_falling_interrupt():
    gpio = FakeGpioAdapter(mode="input", state="high", interrupt_edge="falling")

    gpio.simulate_input_state("low")

    assert gpio.was_interrupt_triggered() is True


# verifies that both edge interrupt triggers
def test_fake_gpio_both_edge_interrupt():
    gpio = FakeGpioAdapter(mode="input", state="low", interrupt_edge="both")

    gpio.simulate_input_state("high")

    assert gpio.was_interrupt_triggered() is True


# verifies that interrupt can be cleared
def test_fake_gpio_clear_interrupt():
    gpio = FakeGpioAdapter(mode="input", state="low", interrupt_edge="rising")

    gpio.simulate_input_state("high")
    gpio.clear_interrupt()

    assert gpio.was_interrupt_triggered() is False


# verifies that gpio state is returned
def test_fake_gpio_state():
    gpio = FakeGpioAdapter(
        mode="input",
        state="low",
        pull="pull_up",
        interrupt_edge="both",
    )

    state = gpio.get_state()

    assert state["mode"] == "input"
    assert state["state"] == "low"
    assert state["pull"] == "pull_up"
    assert state["interrupt_edge"] == "both"