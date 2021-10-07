'''
Software Sales
1. Input = Amount of packages purchased.
2. Calculate subtotal, discount percentage, discount total and total based on the table. (Discount is calculated using if functions)
3. Output = Display subtotal, discount percent, discount total, and total.
4. Output = Return an error if input is negative. Proceeds to then terminate the program after a few seconds.
'''
from time import sleep

a = int(input("Enter the amount of packages purchased: "))

subtotal = a * 99
if 0  <= a < 10:
    disc_percent = 0
elif 10 <= a < 20:
    disc_percent = 10
elif 20 <= a < 50:
    disc_percent = 20
elif 50 <= a < 100:
    disc_percent = 30
elif a >= 100:
    disc_percent = 40
else:
    print("Calculation Error!"); sleep(1.3)
    print("This program will now terminate!"); sleep(1.6)
    quit()

disc_total = subtotal * (disc_percent/100)
total = subtotal - disc_total


print("Subtotal: $99.00 x {0} = ${1:0.2f}".format(a, subtotal))
print("Discount amount @ {0}% = ${1:0.2f}".format(disc_percent, disc_total))
print("Total amount:           ${0:0.2f}".format(total))