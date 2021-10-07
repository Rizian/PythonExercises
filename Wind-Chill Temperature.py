'''
Wind-Chill Temperature
1. Input = Two variables: Temperature and Wind speed.
2. Validate whether or not variable values is within the given range for formula. If yes, continue; if no, 5.
3. Calculate Wind_Chill_Temp using the formula.
4. Output = Return Wind_Chill_Temp. End
5. Output = Return and error and prompt to try again. Go to 1.
'''
from math import pow

def main():
    Temp = eval(input("Enter the temperature in Fahrenheit: "))
    v = eval(input("Enter the wind speed in mph: "))
    
    if (-58 <= Temp <= 41) and (v >= 2):
        WCTemp = 35.74 + 0.6215 * Temp - 35.75 * pow(v, 0.16) + 0.4275 * Temp * pow(v, 0.16)

        print("The wind chill index is {0:0.3f}".format(WCTemp))
    else:
        if (Temp > 41 or Temp < -58) and v < 2:
            print("Temperature must be between -58 and 41 Fahrenheit and\nthe wind speed has to be greater than or equal to 2 mph")
        elif Temp > 41 or Temp < -58:
            print("Temperature must be between -58 and 41 Fahrenheit")
        elif v < 2:
            print("The wind speed has to be greater than or equal to 2 mph")
        main()

main()

