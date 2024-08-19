Title: Battery Power Miscalculation at Specific Throttle Levels

Severity: Critical

Priority: High

Description:
When the throttle is set to any level ending in '3' (e.g., 3, 13, 23, etc.), the battery incorrectly outputs 30 watts of power, regardless of the expected value. This causes a significant drop in power and speed, leading to a "bucking" effect in the car's acceleration.

Steps to Reproduce:

1. Set the throttle to a level ending in '3' (e.g., 3, 13, 23, etc.).
2. Observe the battery power output.
3. Note that the power output is always 30 watts.

Expected Result:
The battery should output a power level corresponding to the throttle input, with a smooth increase in power as the throttle level increases.

Actual Result:
The battery outputs 30 watts of power whenever the throttle level ends in '3'.

Reproducibility: 100%

Environment:

- Battery Firmware Version: 1.0.0
- Throttle Firmware Version: 1.0.0
- Testing Environment: Lab Simulation

Attachments:

- Screenshots of the battery power output at throttle levels 13, 23, 33, etc.
- Log files showing the power output during the tests.
- Video recording demonstrating the "bucking" effect.