# tests common interface validation behavior

from adapters.base_interface_adapter import BaseInterfaceAdapter
from validators.interface_validator import InterfaceValidator


# verifies connected validation passes
def test_validate_connected_passes():
    adapter = BaseInterfaceAdapter("base")
    validator = InterfaceValidator()

    adapter.connect()
    result = validator.validate_connected(adapter)

    assert result["passed"] is True


# verifies connected validation fails
def test_validate_connected_fails():
    adapter = BaseInterfaceAdapter("base")
    validator = InterfaceValidator()

    result = validator.validate_connected(adapter)

    assert result["passed"] is False


# verifies disconnected validation passes
def test_validate_disconnected_passes():
    adapter = BaseInterfaceAdapter("base")
    validator = InterfaceValidator()

    result = validator.validate_disconnected(adapter)

    assert result["passed"] is True


# verifies disconnected validation fails
def test_validate_disconnected_fails():
    adapter = BaseInterfaceAdapter("base")
    validator = InterfaceValidator()

    adapter.connect()
    result = validator.validate_disconnected(adapter)

    assert result["passed"] is False


# verifies range validation passes
def test_validate_range_passes():
    validator = InterfaceValidator()

    result = validator.validate_range("range_test", 5, 0, 10)

    assert result["passed"] is True


# verifies range validation fails
def test_validate_range_fails():
    validator = InterfaceValidator()

    result = validator.validate_range("range_test", 20, 0, 10)

    assert result["passed"] is False


# verifies limit validation passes
def test_validate_limit_passes():
    validator = InterfaceValidator()

    result = validator.validate_limit("limit_test", 5, 10)

    assert result["passed"] is True


# verifies limit validation fails
def test_validate_limit_fails():
    validator = InterfaceValidator()

    result = validator.validate_limit("limit_test", 20, 10)

    assert result["passed"] is False


# verifies equality validation passes
def test_validate_equal_passes():
    validator = InterfaceValidator()

    result = validator.validate_equal("equal_test", "high", "high")

    assert result["passed"] is True


# verifies equality validation fails
def test_validate_equal_fails():
    validator = InterfaceValidator()

    result = validator.validate_equal("equal_test", "high", "low")

    assert result["passed"] is False


# verifies result summary
def test_summarize_results():
    validator = InterfaceValidator()
    results = [
        {"passed": True},
        {"passed": True},
        {"passed": False},
    ]

    summary = validator.summarize_results(results)

    assert summary["total"] == 3
    assert summary["passed"] == 2
    assert summary["failed"] == 1
    assert summary["success_rate"] == 2 / 3