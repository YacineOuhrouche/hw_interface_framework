# tests full automation flow from pipeline to report generation

import json
from pathlib import Path

from automation.regression_runner import run_regression
from automation.validation_pipeline import run_all_pipelines


# verifies all validation pipelines pass
def test_all_pipelines_pass():
    result = run_all_pipelines()

    assert result["status"] == "PASS"
    assert len(result["pipelines"]) == 5


# verifies regression creates a valid report file
def test_regression_creates_report():
    output_path = run_regression()
    path = Path(output_path)

    assert path.exists()

    with path.open("r", encoding="utf-8") as file:
        report = json.load(file)

    assert report["interface"] == "hardware_interface"
    assert report["status"] == "PASS"
    assert report["total_tests"] == report["passed_tests"]
    assert report["failed_tests"] == 0