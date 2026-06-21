# tests the fake dac adapter behavior

from adapters.fake_dac_adapter import FakeDacAdapter


# verifies that the fake dac starts with the expected configuration
def test_fake_dac_configuration():
    dac = FakeDacAdapter(
        resolution_bits=12,
        reference_voltage=3.3,
    )

    assert dac.resolution_bits == 12
    assert dac.reference_voltage == 3.3


# verifies that the fake dac returns the correct max code
def test_fake_dac_max_code():
    dac = FakeDacAdapter(resolution_bits=12)

    assert dac.get_max_code() == 4095


# verifies that voltage is converted to code
def test_fake_dac_voltage_to_code():
    dac = FakeDacAdapter(resolution_bits=12, reference_voltage=3.3)

    code = dac.voltage_to_code(1.65)

    assert code in [2047, 2048]


# verifies that code is converted to voltage
def test_fake_dac_code_to_voltage():
    dac = FakeDacAdapter(resolution_bits=12, reference_voltage=3.3)

    voltage = dac.code_to_voltage(4095)

    assert voltage == 3.3


# verifies that low voltage is clamped
def test_fake_dac_low_voltage_clamp():
    dac = FakeDacAdapter(reference_voltage=3.3)

    code = dac.write_voltage(-1.0)

    assert code == 0
    assert dac.read_output_voltage() == 0.0


# verifies that high voltage is clamped
def test_fake_dac_high_voltage_clamp():
    dac = FakeDacAdapter(reference_voltage=3.3)

    code = dac.write_voltage(5.0)

    assert code == 4095
    assert dac.read_output_voltage() == 3.3


# verifies that low code is clamped
def test_fake_dac_low_code_clamp():
    dac = FakeDacAdapter(reference_voltage=3.3)

    voltage = dac.write_code(-10)

    assert dac.read_output_code() == 0
    assert voltage == 0.0


# verifies that high code is clamped
def test_fake_dac_high_code_clamp():
    dac = FakeDacAdapter(reference_voltage=3.3)

    voltage = dac.write_code(5000)

    assert dac.read_output_code() == 4095
    assert voltage == 3.3


# verifies that writing voltage updates the dac state
def test_fake_dac_write_voltage_updates_state():
    dac = FakeDacAdapter(reference_voltage=3.3)

    dac.write_voltage(1.65)

    assert dac.read_output_code() in [2047, 2048]
    assert abs(dac.read_output_voltage() - 1.65) < 0.001


# verifies that writing code updates the dac state
def test_fake_dac_write_code_updates_state():
    dac = FakeDacAdapter(reference_voltage=3.3)

    dac.write_code(2048)

    assert dac.read_output_code() == 2048
    assert abs(dac.read_output_voltage() - 1.65) < 0.01