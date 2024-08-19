# Bug Report for Electric Car Battery and Throttle System

# Overview
This repository contains a bug report for the interaction between the throttle and the battery in an electric car, specifically regarding an issue where the battery produces incorrect power outputs at certain throttle levels. The report provides details about the observed issue, the testing performed, and suggestions for further investigation and resolution.

# Files
**Bug_Report(Task_2).md:** The detailed bug report describing the issue, steps to reproduce, expected vs. actual behavior, and potential impact.

# Bug Description
**Summary:**
 Issue: When the throttle level ends in "3" (e.g., 3 km/h, 13 km/h, 23 km/h, etc.), the battery erroneously outputs 30 watts of power, regardless of the throttle level. This results in unexpected power drops and potential safety risks, such as the car "bucking" during acceleration.

# Steps to Reproduce:
1.	Set the throttle level to any value ending in "3" (e.g., 3 km/h, 13 km/h, 53 km/h).
2.	Observe the power output from the battery.
   
**Expected Behavior:**
•	The battery should generate power corresponding to the throttle level, following a linear relationship between 0 watts (at 0 km/h) and 1000 watts (at 250 km/h).

**Actual Behavior:**
•	The battery consistently outputs 30 watts of power whenever the throttle level ends in "3", regardless of the actual throttle level.

**Impact:**
•	This bug causes erratic car behavior during acceleration, potentially leading to safety issues, including sudden loss of speed and control.

# Testing and Reproduction Steps
The bug report includes a comprehensive set of test scenarios to validate the issue:

**Reproduction Tests:**

•	**Throttle at 3 km/h:**

o	Expected: 12 watts

o	Actual: 30 watts

•	**Throttle at 13 km/h:**

o	Expected: 52 watts

o	Actual: 30 watts

•	**Throttle at 53 km/h:**

o	Expected: 212 watts

o	Actual: 30 watts

•	**Throttle at 103 km/h:**

o	Expected: 412 watts

o	Actual: 30 watts

**Non-Affected Tests:**

•	**Throttle at 10 km/h:**

o	Expected: 40 watts

o	Actual: 40 watts

•	**Throttle at 20 km/h:**

o	Expected: 80 watts

o	Actual: 80 watts

These tests confirm the presence of the bug at specific throttle levels and show that the issue is isolated to cases where the throttle level ends in "3".

# Suggested Investigation
The bug report recommends the following steps for further investigation:
1.	Code Review: Inspect the code handling throttle input and battery output to identify any conditional logic or rounding errors that may cause this bug.
2.	Boundary Testing: Perform additional boundary testing around the affected throttle levels to identify any patterns or edge cases.
3.	Simulation: Run simulations to observe the impact of this bug over time and under various driving conditions.
4.	Collaboration: Work with the development team to replicate the issue in a controlled environment and explore potential fixes.

