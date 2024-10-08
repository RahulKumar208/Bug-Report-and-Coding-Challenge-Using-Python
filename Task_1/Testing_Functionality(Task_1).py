# BATTERY POWER

def battery_power(throttle_level):
    
    # Check for invalid throttle levels
    if throttle_level < 0 or throttle_level > 250:
        raise ValueError("Invalid throttle level: Must be between 0 and 250 km/h")
    
    # Calculate the power level of the battery
    power_level = (throttle_level / 250) * 1000
    
    return power_level


# Example Test Cases
print(battery_power(0))      # Expected output: 0 watts (Throttle at MIN LEVEL)
print(battery_power(125))    # Expected output: 500 watts (Throttle at mid-level)
print(battery_power(250))    # Expected output: 1000 watts (Throttle at MAX LEVEL)



#TEST BATTERY POWER

# Boundary Tests
assert battery_power(0) == 0.0     # Throttle at MIN LEVEL
assert battery_power(250) == 1000.0 # Throttle at MAX LEVEL

# Mid-Range Tests
assert battery_power(125) == 500.0  # Throttle at half-max
assert battery_power(50) == 200.0   # Throttle at 20% max
assert battery_power(200) == 800.0  # Throttle at 80% max


# Fail States
try:
    battery_power(-10)
except ValueError as e:
    print(e)  # Expect an error message for invalid throttle level

try:
    battery_power(300)
except ValueError as e:
    print(e)  # Expect an error message for invalid throttle level

try:
    battery_power("100")
except ValueError as e:
    print(e)  # Expect an error message for invalid input type