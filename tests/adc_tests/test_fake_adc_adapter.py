# tests the fake adc adapter behavior

from adapters.fake_adc_adapter import FakeAdcAdapter


# verifies that the fake adc starts with the expected configuration
def test_fake_adc_configuration():
    adc = FakeAdcAdapter(
        resolution_bits=12,
        reference_voltage=3.3,
        input_voltage=1.65,
    )

    assert adc.resolution_bits == 12
    assert adc.reference_voltage == 3.3
    assert adc.input_voltage == 1.65


# verifies that the fake adc returns the correct max code
def test_fake_adc_max_code():
    adc = FakeAdcAdapter(resolution_bits=12)

    assert adc.get_max_code() == 4095


# verifies that voltage is converted to code
def test_fake_adc_voltage_to_code():
    adc = FakeAdcAdapter(resolution_bits=12, reference_voltage=3.3)

    code = adc.voltage_to_code(1.65)

    assert code in [2047, 2048]


# verifies that code is converted to voltage
def test_fake_adc_code_to_voltage():
    adc = FakeAdcAdapter(resolution_bits=12, reference_voltage=3.3)

    voltage = adc.code_to_voltage(4095)

    assert voltage == 3.3


# verifies that low voltage is clamped
def test_fake_adc_low_voltage_clamp():
    adc = FakeAdcAdapter(reference_voltage=3.3)

    code = adc.voltage_to_code(-1.0)

    assert code == 0


# verifies that high voltage is clamped
def test_fake_adc_high_voltage_clamp():
    adc = FakeAdcAdapter(reference_voltage=3.3)

    code = adc.voltage_to_code(5.0)

    assert code == 4095


# verifies that sample reading returns the expected count
def test_fake_adc_sample_count():
    adc = FakeAdcAdapter(input_voltage=1.65)

    samples = adc.read_samples(10)

    assert len(samples) == 10