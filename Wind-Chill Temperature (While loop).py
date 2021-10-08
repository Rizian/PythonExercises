'''
Wind-Chill Temperature
1. Input = Two variables: Temperature and Wind speed.
2. Validate whether or not variable values is within the given range for formula. If yes, continue; if no, 5.
3. Calculate Wind_Chill_Temp using the formula.
4. Output = Return Wind_Chill_Temp. End
5. Output = Return and error and prompt to try again. Go to 1.
'''
from math import pow

Temp = eval(input("Enter the temperature in Fahrenheit: "))

while Temp < -58 or Temp > 41:
    Temp = eval(input("Please Re-enter the temperature (has to be between -58F and 41F): "))

v = eval(input("Enter the wind speed in mph: "))

while v < 2:
    v = eval(input("Please Re-enter the wind speed (has to be greater than or equal to 2 mph: "))

WCTemp = 35.74 + 0.6215 * Temp - 35.75 * pow(v, 0.16) + 0.4275 * Temp * pow(v, 0.16)

print("The wind chill index is {0:0.3f}".format(WCTemp))