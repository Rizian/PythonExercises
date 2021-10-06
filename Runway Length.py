'''
Runway Length

1. Input = 2 float variables a and v for acceleration and take-off speed respectively
2. Calculate and store the minimum required runway length value using the formula v**2/2a
3. Output = Returns the value formatted to 4 decimal places.
'''

v = float(input("Enter the plane's take-off speed in m/s: "))
a = float(input("Enter the plane's acceleration in m/s^2: "))

length = v**2/(2*a)

print(f"The minimum required runway length for this airplane is {length:0.4} meters.")