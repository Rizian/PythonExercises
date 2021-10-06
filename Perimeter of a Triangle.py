'''
Perimeter of a Triangle

1. Input = 3 float variables, one for each side of the triangle.
3. check if the sum of two sides is greater than the one remaining side; if yes = 4.; If no = 5.
4. Output = Calculate the sum of all three sides and return the value.
5. Output = Returns an error message.
'''

print("Triangle Perimeter")
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print(f"The perimeter of the triangle is {side1+side2+side3}!")
else:
    print("invalid input. Values don't represent a triangle and cannot be calculated!")