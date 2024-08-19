# Battery Power Simulation

# Overview
This repository contains a Python function that simulates the interaction between a throttle and a battery in an electric car. The function, battery_power, calculates the power output of the battery based on the throttle level. The throttle controls the speed of the car, and the battery provides the corresponding power needed for that speed.

The project includes both the implementation of the function and the test cases to ensure its correctness.

# Files
- Testing_Functionality(Task_1).py: Contains the main function battery_power and associated test cases.

# Function Details
battery_power(throttle_level)

# Parameters:
**throttle_level:** An integer or float representing the level of the throttle (in km/h). It must be between 0 and 250.

# Returns:
**power_level:** A float representing the power output of the battery (in watts). The output is proportional to the throttle level, ranging from 0 watts (at 0 km/h) to 1000 watts (at 250 km/h).

# Description:

The function checks if the throttle_level is within the valid range (0-250 km/h). If the input is valid, it calculates the power level using a linear relationship between throttle level and power. If the input is invalid, it raises a ValueError.

# Example Usage:
print(battery_power(0))      # Expected output: 0 watts (Throttle at MIN LEVEL)
print(battery_power(125))    # Expected output: 500 watts (Throttle at mid-level)
print(battery_power(250))    # Expected output: 1000 watts (Throttle at MAX LEVEL)

# Testing
The Testing_Functionality(Task_1).py file also contains a set of test cases to validate the function:

# Boundary Tests:
•	Throttle at MIN LEVEL (0 km/h): 
  o	assert battery_power(0) == 0.0
•	Throttle at MAX LEVEL (250 km/h): 
  o	assert battery_power(250) == 1000.0

# Mid-Range Tests:
•	Throttle at 125 km/h (50% of MAX): 
  o	assert battery_power(125) == 500.0
•	Throttle at 50 km/h (20% of MAX): 
  o	assert battery_power(50) == 200.0
•	Throttle at 200 km/h (80% of MAX): 
  o	assert battery_power(200) == 800.0

# Fail States:
•	Invalid Throttle Level (Negative):
o Test: battery_power(-10)
o Expected: Raises ValueError with message "Invalid throttle level: Must be between 0 and 250 km/h"

•	Invalid Throttle Level (Above 250 km/h):
  o	Test: battery_power(300)
  o	Expected: Raises ValueError with message "Invalid throttle level: Must be between 0 and 250 km/h"

•	Invalid Input Type (Non-numeric):
  o	Test: battery_power("100")
  o	Expected: Raises TypeError

# Running Tests
To run the test cases, simply execute the script. If the function works as expected, the assertions will pass without errors. If any test fails, the script will raise an assertion error.
