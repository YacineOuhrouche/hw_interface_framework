# tests saturation analyzer behavior

import pytest

from analyzers.saturation_analyzer import SaturationAnalyzer


# verifies low saturation counting
def test_count_low_saturation():
    analyzer = SaturationAnalyzer()
    samples = [0.0, 0.0, 1.0, 2.0]

    result = analyzer.count_low_saturation(samples, 0.0)

    assert result == 2


# verifies high saturation counting
def test_count_high_saturation():
    analyzer = SaturationAnalyzer()
    samples = [1.0, 2.0, 3.3, 3.3]

    result = analyzer.count_high_saturation(samples, 3.3)

    assert result == 2


# verifies total saturation counting
def test_count_total_saturation():
    analyzer = SaturationAnalyzer()
    samples = [0.0, 1.0, 3.3, 3.3]

    result = analyzer.count_total_saturation(samples, 0.0, 3.3)

    assert result == 3


# verifies saturation percentage calculation
def test_calculate_saturation_percent():
    analyzer = SaturationAnalyzer()
    samples = [0.0, 1.0, 3.3, 3.3]

    result = analyzer.calculate_saturation_percent(samples, 0.0, 3.3)

    assert result == pytest.approx(75.0)


# verifies complete saturation analysis
def test_saturation_analysis():
    analyzer = SaturationAnalyzer()
    samples = [0.0, 1.0, 3.3, 3.3]

    result = analyzer.analyze(samples, 0.0, 3.3)

    assert result["analysis"] == "saturation"
    assert result["sample_count"] == 4
    assert result["low_saturation_count"] == 1
    assert result["high_saturation_count"] == 2
    assert result["total_saturation_count"] == 3
    assert result["saturation_percent"] == pytest.approx(75.0)