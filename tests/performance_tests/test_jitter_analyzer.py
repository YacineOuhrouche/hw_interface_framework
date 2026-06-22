# tests jitter analyzer behavior

import pytest

from analyzers.jitter_analyzer import JitterAnalyzer


# verifies average period calculation
def test_jitter_average_period():
    analyzer = JitterAnalyzer()

    result = analyzer.calculate_average_period([1000.0, 1001.0, 999.0])

    assert result == pytest.approx(1000.0)


# verifies peak to peak jitter calculation
def test_jitter_peak_to_peak():
    analyzer = JitterAnalyzer()

    result = analyzer.calculate_peak_to_peak_jitter([1000.0, 1001.0, 999.0])

    assert result == pytest.approx(2.0)


# verifies maximum absolute jitter calculation
def test_jitter_max_absolute():
    analyzer = JitterAnalyzer()

    result = analyzer.calculate_max_absolute_jitter([1000.0, 1001.0, 999.0])

    assert result == pytest.approx(1.0)


# verifies complete jitter analysis
def test_jitter_analysis():
    analyzer = JitterAnalyzer()

    result = analyzer.analyze([1000.0, 1001.0, 999.0])

    assert result["analysis"] == "jitter"
    assert result["sample_count"] == 3
    assert result["average_period"] == pytest.approx(1000.0)
    assert result["peak_to_peak_jitter"] == pytest.approx(2.0)
    assert result["max_absolute_jitter"] == pytest.approx(1.0)