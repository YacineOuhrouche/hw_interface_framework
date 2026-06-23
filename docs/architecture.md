# Architecture

The framework is organized into modular components.

## Adapters

Provide hardware interface access.

adapters/

Examples:

* FakeAdcAdapter
* FakeDacAdapter
* FakePwmAdapter
* FakeEncoderAdapter
* FakeGpioAdapter

## Validators

Validate interface behavior.

validators/

Examples:

* ADC validation
* DAC validation
* PWM validation
* Encoder validation
* GPIO validation

## Analyzers

Analyze measurement data.

analyzers/

Examples:

* Noise analysis
* Drift analysis
* Timing analysis
* Jitter analysis
* Saturation analysis

## Fault Injection

Simulate interface failures.

fault_injection/

Examples:

* ADC noise injection
* ADC saturation
* PWM timing faults
* Encoder pulse loss
* GPIO glitches

## Diagnostics

Detect interface failures.

diagnostics/

Examples:

* Signal trace analysis
* Failure classification
* Timing violation detection

## Automation

Execute validation workflows and generate reports.

automation/