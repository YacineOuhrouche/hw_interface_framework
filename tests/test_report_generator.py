# tests hardware interface report generation

import json

from automation.report_generator import (
    create_report,
    generate_default_report,
    save_report,
)


# verifies report creation
def test_create_report():
    report = create_report(
        interface="adc",
        total_tests=3,
        passed_tests=2,
        failed_tests=1,
        faults_injected=1,
        timing_checks=0,
        noise_checks=1,
    )

    assert report["interface"] == "adc"
    assert report["total_tests"] == 3
    assert report["passed_tests"] == 2
    assert report["failed_tests"] == 1
    assert report["status"] == "FAIL"


# verifies passing report status
def test_create_passing_report():
    report = create_report(
        interface="pwm",
        total_tests=2,
        passed_tests=2,
        failed_tests=0,
    )

    assert report["status"] == "PASS"


# verifies report saving
def test_save_report(tmp_path):
    report = create_report(
        interface="gpio",
        total_tests=1,
        passed_tests=1,
        failed_tests=0,
    )

    output_path = tmp_path / "gpio_report.json"
    saved_path = save_report(report, str(output_path))

    with open(saved_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["interface"] == "gpio"
    assert data["status"] == "PASS"


# verifies default report generation
def test_generate_default_report():
    output_path = generate_default_report()

    assert output_path == "reports/hardware_interface_report.json"