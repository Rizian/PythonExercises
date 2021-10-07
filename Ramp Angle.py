'''
Ramp Angle
1. Store constant g = 9.8m/s.
2. Input = Float values for mass of cart and Force needed to push cart.
3. Calculate and store angle value using formula (with math.asin functions in radians).
4. Convert the value to degrees.
5. Return the value.
'''
from math import asin, degrees
g = 9.8

m = float(input("Enter the mass of the cart (in kg): "))
F = float(input("Enter the force needed to push the cart (in N): "))

angle = asin(F/(m*g))
angle = degrees(angle)
print("The angle of the ramp is {0:0.1f} degrees.".format(angle))