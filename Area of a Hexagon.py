'''
Area of a Hexagon
1. Input = Side length of the hexagon.
2. Calculate and store the area of the hexagon using formula.
3. Output = Return the area value formatted to 3 decimal places.
'''
from math import pow, sqrt

side = float(input("Enter the length of the side of the hexagon: "))

area = (3*sqrt(3)/2)*pow(side, 2)

print("The area of a hexagon of side length {0} is {1:0.3f}.".format(side, area))