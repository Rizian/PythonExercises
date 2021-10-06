'''
Slope of a line

1. Input = x1,x2,y1,y2
2. convert all variables to floats
3. calculate and store value on var slope
4. Output = return slope value to 5 decimal places
'''

x1, y1 = input("Enter the coordinates of point 1 (x, y): ").split(sep=", ")
x2, y2 = input("Enter the coordinates of point 2 (x, y): ").split(sep=", ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

slope = (y2 - y1) / (x2 - x1)

print("The slope of between the two points is {0:0.5f}.".format(slope))