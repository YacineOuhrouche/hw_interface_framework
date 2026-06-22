# tests hardware interface regression runner

import json
from pathlib import Path

from automation.regression_runner import (
    collect_results,
    count_passed_tests,
    count_total_tests,
    run_regression,
)


# verifies total test counting
def test_count_total_tests():
    pipelines = [
        {
            "interface": "adc",
            "accuracy_valid": True,
            "range_valid": True,
        },
        {
            "interface": "pwm",
            "frequency_valid": True,
        },
    ]

    result = count_total_tests(pipelines)

    assert result == 3


# verifies passed test counting
def test_count_passed_tests():
    pipelines = [
        {
            "interface": "adc",
            "accuracy_valid": True,
            "range_valid": False,
        },
        {
            "interface": "pwm",
            "frequency_valid": True,
        },
    ]

    result = count_passed_tests(pipelines)

    assert result == 2


# verifies result collection
def test_collect_results():
    result = collect_results()

    assert result["interface"] == "hardware_interface"
    assert result["total_tests"] > 0
    assert result["passed_tests"] == result["total_tests"]
    assert result["failed_tests"] == 0
    assert result["status"] == "PASS"


# verifies regression report generation
def test_run_regression():
    output_path = run_regression()
    path = Path(output_path)

    assert path.exists()

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["interface"] == "hardware_interface"
    assert data["status"] == "PASS"