# tests noise analyzer behavior

from analyzers.noise_analyzer import NoiseAnalyzer


# verifies mean calculation
def test_noise_analyzer_mean():
    analyzer = NoiseAnalyzer()
    samples = [1.0, 2.0, 3.0]

    result = analyzer.calculate_mean(samples)

    assert result == 2.0


# verifies peak to peak calculation
def test_noise_analyzer_peak_to_peak():
    analyzer = NoiseAnalyzer()
    samples = [1.0, 1.5, 2.0]

    result = analyzer.calculate_peak_to_peak(samples)

    assert result == 1.0


# verifies standard deviation calculation
def test_noise_analyzer_standard_deviation():
    analyzer = NoiseAnalyzer()
    samples = [1.0, 1.0, 1.0]

    result = analyzer.calculate_standard_deviation(samples)

    assert result == 0.0


# verifies peak noise calculation
def test_noise_analyzer_peak_noise():
    analyzer = NoiseAnalyzer()
    samples = [1.0, 2.0, 3.0]

    result = analyzer.calculate_peak_noise(samples)

    assert result == 1.0


# verifies full noise analysis
def test_noise_analyzer_analyze():
    analyzer = NoiseAnalyzer()
    samples = [1.0, 2.0, 3.0]

    result = analyzer.analyze(samples)

    assert result["analysis"] == "noise"
    assert result["sample_count"] == 3
    assert result["mean"] == 2.0
    assert result["peak_to_peak"] == 2.0
    assert result["peak_noise"] == 1.0