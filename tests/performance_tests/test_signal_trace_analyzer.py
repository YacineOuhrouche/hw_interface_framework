# tests signal trace analyzer behavior

from diagnostics.signal_trace_analyzer import SignalTraceAnalyzer


# verifies transition counting
def test_signal_trace_transition_count():
    analyzer = SignalTraceAnalyzer()
    samples = ["low", "low", "high", "high", "low"]

    result = analyzer.count_transitions(samples)

    assert result == 2


# verifies transition index detection
def test_signal_trace_transition_indexes():
    analyzer = SignalTraceAnalyzer()
    samples = ["low", "low", "high", "high", "low"]

    result = analyzer.find_transition_indexes(samples)

    assert result == [2, 4]


# verifies stable signal detection
def test_signal_trace_stable():
    analyzer = SignalTraceAnalyzer()
    samples = ["high", "high", "high"]

    result = analyzer.is_stable(samples)

    assert result is True


# verifies unstable signal detection
def test_signal_trace_unstable():
    analyzer = SignalTraceAnalyzer()
    samples = ["high", "low", "high"]

    result = analyzer.is_stable(samples)

    assert result is False


# verifies complete signal trace analysis
def test_signal_trace_analysis():
    analyzer = SignalTraceAnalyzer()
    samples = ["low", "low", "high", "high", "low"]

    result = analyzer.analyze(samples)

    assert result["analysis"] == "signal_trace"
    assert result["sample_count"] == 5
    assert result["transition_count"] == 2
    assert result["transition_indexes"] == [2, 4]
    assert result["stable"] is False