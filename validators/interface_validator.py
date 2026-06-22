# validates common interface status results and limit checks


class InterfaceValidator:
    # stores shared interface validation settings
    def __init__(self, config=None):
        self.config = config or {}

    # validates that an adapter is connected
    def validate_connected(self, adapter):
        connected = adapter.is_connected()

        return {
            "test": "interface_connected",
            "passed": connected is True,
            "adapter": adapter.name,
            "connected": connected,
        }

    # validates that an adapter is disconnected
    def validate_disconnected(self, adapter):
        connected = adapter.is_connected()

        return {
            "test": "interface_disconnected",
            "passed": connected is False,
            "adapter": adapter.name,
            "connected": connected,
        }

    # validates that a value is inside a minimum and maximum range
    def validate_range(self, test_name, value, minimum, maximum):
        return {
            "test": test_name,
            "passed": minimum <= value <= maximum,
            "value": value,
            "minimum": minimum,
            "maximum": maximum,
        }

    # validates that a value is below or equal to a limit
    def validate_limit(self, test_name, value, limit):
        return {
            "test": test_name,
            "passed": value <= limit,
            "value": value,
            "limit": limit,
        }

    # validates that a value matches an expected value
    def validate_equal(self, test_name, expected, measured):
        return {
            "test": test_name,
            "passed": measured == expected,
            "expected": expected,
            "measured": measured,
        }

    # summarizes validation results
    def summarize_results(self, results):
        total = len(results)
        passed = sum(1 for result in results if result["passed"])
        failed = total - passed

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "success_rate": passed / total if total > 0 else 0,
        }