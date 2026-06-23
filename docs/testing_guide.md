# Testing Guide

## Test Structure

tests/

├── adc_tests/
├── dac_tests/
├── pwm_tests/
├── encoder_tests/
├── gpio_tests/
├── performance_tests/
├── integration_tests/

## Run All Tests

pytest

## Run One Test File

pytest tests/adc_tests/test_adc_validator.py

## Adding Tests

1. Create a new test file.
2. Add validation scenarios.
3. Execute pytest.
4. Verify results.

## Regression Testing

python -m automation.regression_runner