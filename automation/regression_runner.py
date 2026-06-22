# executes hardware interface validation regression tests

from automation.report_generator import (
    create_report,
    save_report,
)
from automation.validation_pipeline import (
    pipeline_passed,
    run_all_pipelines,
)


# counts total validation checks
def count_total_tests(pipelines):
    total = 0

    for pipeline in pipelines:
        total += len(
            [
                value
                for key, value in pipeline.items()
                if key != "interface"
            ]
        )

    return total


# counts passed validation checks
def count_passed_tests(pipelines):
    passed = 0

    for pipeline in pipelines:
        passed += len(
            [
                value
                for key, value in pipeline.items()
                if key != "interface" and value is True
            ]
        )

    return passed


# collects hardware interface validation results
def collect_results():
    pipeline_results = run_all_pipelines()
    pipelines = pipeline_results["pipelines"]
    total_tests = count_total_tests(pipelines)
    passed_tests = count_passed_tests(pipelines)
    failed_tests = total_tests - passed_tests

    return {
        "interface": "hardware_interface",
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "pipelines": pipelines,
        "status": pipeline_results["status"],
    }


# executes the regression run
def run_regression():
    results = collect_results()

    report = create_report(
        interface=results["interface"],
        total_tests=results["total_tests"],
        passed_tests=results["passed_tests"],
        failed_tests=results["failed_tests"],
        faults_injected=0,
        timing_checks=5,
        noise_checks=1,
        results=results["pipelines"],
    )

    output_path = "reports/hardware_interface_validation_report.json"

    save_report(
        report,
        output_path,
    )

    return output_path


# starts regression execution
def main():
    output_path = run_regression()

    print(f"report generated: {output_path}")


if __name__ == "__main__":
    main()