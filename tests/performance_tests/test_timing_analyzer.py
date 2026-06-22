# tests timing analyzer behavior

import pytest

from analyzers.timing_analyzer import TimingAnalyzer


# verifies average timing calculation
def test_timing_average():
    analyzer = TimingAnalyzer()

    result = analyzer.calculate_average_time(
        [10.0, 20.0, 30.0]
    )

    assert result == pytest.approx(20.0)


# verifies minimum timing calculation
def test_timing_minimum():
    analyzer = TimingAnalyzer()

    result = analyzer.calculate_min_time(
        [10.0, 20.0, 30.0]
    )

    assert result == 10.0


# verifies maximum timing calculation
def test_timing_maximum():
    analyzer = TimingAnalyzer()

    result = analyzer.calculate_max_time(
        [10.0, 20.0, 30.0]
    )

    assert result == 30.0


# verifies timing spread calculation
def test_timing_spread():
    analyzer = TimingAnalyzer()

    result = analyzer.calculate_spread(
        [10.0, 20.0, 30.0]
    )

    assert result == pytest.approx(20.0)


# verifies complete timing analysis
def test_timing_analysis():
    analyzer = TimingAnalyzer()

    result = analyzer.analyze(
        [10.0, 20.0, 30.0]
    )

    assert result["analysis"] == "timing"
    assert result["sample_count"] == 3
    assert result["average_time"] == pytest.approx(20.0)
    assert result["minimum_time"] == 10.0
    assert result["maximum_time"] == 30.0