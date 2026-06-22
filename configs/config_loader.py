# loads yaml configuration files for hardware interface validation

from pathlib import Path
from typing import Any, Dict

import yaml


# loads a yaml config file
def load_config(config_path: str) -> Dict[str, Any]:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"config file not found: {config_path}")

    with path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        return {}

    return config


# loads the adc configuration section
def load_adc_config(
    config_path: str = "configs/adc_config.yaml",
) -> Dict[str, Any]:
    config = load_config(config_path)

    if "adc" not in config:
        raise KeyError("missing adc config section")

    return config["adc"]


# loads the dac configuration section
def load_dac_config(
    config_path: str = "configs/dac_config.yaml",
) -> Dict[str, Any]:
    config = load_config(config_path)

    if "dac" not in config:
        raise KeyError("missing dac config section")

    return config["dac"]


# loads the pwm configuration section
def load_pwm_config(
    config_path: str = "configs/pwm_config.yaml",
) -> Dict[str, Any]:
    config = load_config(config_path)

    if "pwm" not in config:
        raise KeyError("missing pwm config section")

    return config["pwm"]


# loads the encoder configuration section
def load_encoder_config(
    config_path: str = "configs/encoder_config.yaml",
) -> Dict[str, Any]:
    config = load_config(config_path)

    if "encoder" not in config:
        raise KeyError("missing encoder config section")

    return config["encoder"]


# loads the gpio configuration section
def load_gpio_config(
    config_path: str = "configs/gpio_config.yaml",
) -> Dict[str, Any]:
    config = load_config(config_path)

    if "gpio" not in config:
        raise KeyError("missing gpio config section")

    return config["gpio"]