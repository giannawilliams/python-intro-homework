def celsius_to_fahrenheit(c):
    return round((c * 9/5) + 32,2)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5/9,2)

temp_f_to_c = 72
temp_c_to_f = 0

print(f"{temp_c_to_f}°C is {celsius_to_fahrenheit(temp_c_to_f)}°F")
print(f"{temp_f_to_c}°F is {fahrenheit_to_celsius(temp_f_to_c)}°C")
