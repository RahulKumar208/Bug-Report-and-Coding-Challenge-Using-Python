# Battery Power

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