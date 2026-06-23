# tests automation command line entry points

import subprocess
import sys


# verifies report generator can run as a module
def test_report_generator_cli():
    result = subprocess.run(
        [sys.executable, "-m", "automation.report_generator"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "report generated" in result.stdout


# verifies validation pipeline can run as a module
def test_validation_pipeline_cli():
    result = subprocess.run(
        [sys.executable, "-m", "automation.validation_pipeline"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "PASS" in result.stdout


# verifies regression runner can run as a module
def test_regression_runner_cli():
    result = subprocess.run(
        [sys.executable, "-m", "automation.regression_runner"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "report generated" in result.stdout