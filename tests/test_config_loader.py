# tests yaml configuration loading for hardware interface validation

import pytest

from configs.config_loader import (
    load_adc_config,
    load_config,
    load_dac_config,
    load_encoder_config,
    load_gpio_config,
    load_pwm_config,
)


# verifies that adc config loads
def test_load_adc_config():
    config = load_adc_config()

    assert config["name"] == "fake_adc"


# verifies that dac config loads
def test_load_dac_config():
    config = load_dac_config()

    assert config["name"] == "fake_dac"


# verifies that pwm config loads
def test_load_pwm_config():
    config = load_pwm_config()

    assert config["name"] == "fake_pwm"


# verifies that encoder config loads
def test_load_encoder_config():
    config = load_encoder_config()

    assert config["name"] == "fake_encoder"


# verifies that gpio config loads
def test_load_gpio_config():
    config = load_gpio_config()

    assert config["name"] == "fake_gpio"


# verifies that missing config file raises an error
def test_missing_config_file_raises_error():
    with pytest.raises(FileNotFoundError):
        load_config("configs/missing_config.yaml")


# verifies that missing adc section raises an error
def test_missing_adc_section_raises_error(tmp_path):
    config_file = tmp_path / "bad_adc_config.yaml"
    config_file.write_text("wrong:\n  name: fake_adc\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_adc_config(str(config_file))


# verifies that missing dac section raises an error
def test_missing_dac_section_raises_error(tmp_path):
    config_file = tmp_path / "bad_dac_config.yaml"
    config_file.write_text("wrong:\n  name: fake_dac\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_dac_config(str(config_file))


# verifies that missing pwm section raises an error
def test_missing_pwm_section_raises_error(tmp_path):
    config_file = tmp_path / "bad_pwm_config.yaml"
    config_file.write_text("wrong:\n  name: fake_pwm\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_pwm_config(str(config_file))


# verifies that missing encoder section raises an error
def test_missing_encoder_section_raises_error(tmp_path):
    config_file = tmp_path / "bad_encoder_config.yaml"
    config_file.write_text("wrong:\n  name: fake_encoder\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_encoder_config(str(config_file))


# verifies that missing gpio section raises an error
def test_missing_gpio_section_raises_error(tmp_path):
    config_file = tmp_path / "bad_gpio_config.yaml"
    config_file.write_text("wrong:\n  name: fake_gpio\n", encoding="utf-8")

    with pytest.raises(KeyError):
        load_gpio_config(str(config_file))


# verifies that empty yaml returns empty dict
def test_empty_yaml_returns_empty_dict(tmp_path):
    config_file = tmp_path / "empty_config.yaml"
    config_file.write_text("", encoding="utf-8")

    config = load_config(str(config_file))

    assert config == {}