# tests drift analyzer behavior

import pytest

from analyzers.drift_analyzer import DriftAnalyzer


# verifies total drift calculation
def test_drift_analyzer_total_drift():
    analyzer = DriftAnalyzer()
    samples = [1.0, 1.1, 1.2]

    result = analyzer.calculate_total_drift(samples)

    assert result == pytest.approx(0.2)


# verifies absolute drift calculation
def test_drift_analyzer_absolute_drift():
    analyzer = DriftAnalyzer()
    samples = [1.2, 1.1, 1.0]

    result = analyzer.calculate_absolute_drift(samples)

    assert result == pytest.approx(0.2)


# verifies drift rate calculation
def test_drift_analyzer_drift_rate():
    analyzer = DriftAnalyzer()
    samples = [1.0, 1.1, 1.2]

    result = analyzer.calculate_drift_rate_per_sample(samples)

    assert result == pytest.approx(0.1)


# verifies drift rate is zero for one sample
def test_drift_analyzer_single_sample_rate():
    analyzer = DriftAnalyzer()
    samples = [1.0]

    result = analyzer.calculate_drift_rate_per_sample(samples)

    assert result == 0.0


# verifies full drift analysis
def test_drift_analyzer_analyze():
    analyzer = DriftAnalyzer()
    samples = [1.0, 1.1, 1.2]

    result = analyzer.analyze(samples)

    assert result["analysis"] == "drift"
    assert result["sample_count"] == 3
    assert result["start_value"] == 1.0
    assert result["end_value"] == 1.2
    assert result["total_drift"] == pytest.approx(0.2)