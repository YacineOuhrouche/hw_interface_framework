# tests interface failure classification behavior

from diagnostics.interface_failure_classifier import InterfaceFailureClassifier


# verifies passing result has no failure
def test_classifier_passing_result():
    classifier = InterfaceFailureClassifier()
    result = {
        "test": "adc_accuracy",
        "passed": True,
    }

    failure_type = classifier.classify_result(result)

    assert failure_type == "none"


# verifies known failure is classified
def test_classifier_known_failure():
    classifier = InterfaceFailureClassifier()
    result = {
        "test": "adc_noise",
        "passed": False,
    }

    failure_type = classifier.classify_result(result)

    assert failure_type == "signal_noise_failure"


# verifies unknown failure is classified
def test_classifier_unknown_failure():
    classifier = InterfaceFailureClassifier()
    result = {
        "test": "custom_test",
        "passed": False,
    }

    failure_type = classifier.classify_result(result)

    assert failure_type == "unknown_failure"


# verifies multiple results are classified
def test_classifier_multiple_results():
    classifier = InterfaceFailureClassifier()
    results = [
        {
            "test": "adc_accuracy",
            "passed": True,
        },
        {
            "test": "pwm_jitter",
            "passed": False,
        },
    ]

    classifications = classifier.classify_results(results)

    assert len(classifications) == 2
    assert classifications[0]["failure_type"] == "none"
    assert classifications[1]["failure_type"] == "timing_jitter_failure"


# verifies failed classifications are returned
def test_classifier_get_failures():
    classifier = InterfaceFailureClassifier()
    results = [
        {
            "test": "adc_accuracy",
            "passed": True,
        },
        {
            "test": "gpio_glitch",
            "passed": False,
        },
    ]

    failures = classifier.get_failures(results)

    assert len(failures) == 1
    assert failures[0]["failure_type"] == "glitch_failure"