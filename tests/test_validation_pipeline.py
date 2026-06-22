# tests hardware interface validation pipeline

from automation.validation_pipeline import (
    pipeline_passed,
    run_adc_pipeline,
    run_all_pipelines,
    run_dac_pipeline,
    run_encoder_pipeline,
    run_gpio_pipeline,
    run_pwm_pipeline,
)


# verifies passing pipeline detection
def test_pipeline_passed_true():
    result = {
        "interface": "adc",
        "accuracy_valid": True,
        "range_valid": True,
    }

    assert pipeline_passed(result) is True


# verifies failing pipeline detection
def test_pipeline_passed_false():
    result = {
        "interface": "adc",
        "accuracy_valid": True,
        "range_valid": False,
    }

    assert pipeline_passed(result) is False


# verifies adc pipeline passes
def test_run_adc_pipeline():
    result = run_adc_pipeline()

    assert result["interface"] == "adc"
    assert pipeline_passed(result) is True


# verifies dac pipeline passes
def test_run_dac_pipeline():
    result = run_dac_pipeline()

    assert result["interface"] == "dac"
    assert pipeline_passed(result) is True


# verifies pwm pipeline passes
def test_run_pwm_pipeline():
    result = run_pwm_pipeline()

    assert result["interface"] == "pwm"
    assert pipeline_passed(result) is True


# verifies encoder pipeline passes
def test_run_encoder_pipeline():
    result = run_encoder_pipeline()

    assert result["interface"] == "encoder"
    assert pipeline_passed(result) is True


# verifies gpio pipeline passes
def test_run_gpio_pipeline():
    result = run_gpio_pipeline()

    assert result["interface"] == "gpio"
    assert pipeline_passed(result) is True


# verifies all pipelines pass
def test_run_all_pipelines():
    result = run_all_pipelines()

    assert result["status"] == "PASS"
    assert len(result["pipelines"]) == 5