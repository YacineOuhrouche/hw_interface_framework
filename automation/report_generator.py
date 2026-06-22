# generates hardware interface validation reports in json format

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


# creates a hardware interface validation report
def create_report(
    interface: str,
    total_tests: int,
    passed_tests: int,
    failed_tests: int,
    faults_injected: int = 0,
    timing_checks: int = 0,
    noise_checks: int = 0,
    results: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    return {
        "timestamp": datetime.now().isoformat(),
        "interface": interface,
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "faults_injected": faults_injected,
        "timing_checks": timing_checks,
        "noise_checks": noise_checks,
        "results": results or [],
        "status": "PASS" if failed_tests == 0 else "FAIL",
    }


# saves a validation report to json file
def save_report(report: Dict[str, Any], output_path: str) -> str:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return str(path)


# generates a default hardware interface report
def generate_default_report() -> str:
    report = create_report(
        interface="hardware_interface",
        total_tests=0,
        passed_tests=0,
        failed_tests=0,
    )

    return save_report(report, "reports/hardware_interface_report.json")


# starts report generation from command line
def main() -> None:
    output_path = generate_default_report()

    print(f"report generated: {output_path}")


if __name__ == "__main__":
    main()