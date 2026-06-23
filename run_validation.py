# runs the full hardware interface validation workflow

from automation.regression_runner import run_regression
from automation.validation_pipeline import run_all_pipelines


# runs validation pipeline and report generation
def main():
    results = run_all_pipelines()
    report_path = run_regression()

    print("hardware interface validation complete")
    print(f"status: {results['status']}")
    print(f"report: {report_path}")


if __name__ == "__main__":
    main()