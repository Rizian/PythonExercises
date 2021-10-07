'''
Tip Calculator

1. Input = Subtotal amount and tip (in percentage).
2. Calculate and store the tip amount (Subtotal * tip percentage).
3. Calculate and store the total amount (Subtotal + Tip amount).
4. Format both tip and total amount into 2 decimal places.
5. Output = Return the subtotal, tip amount and total values with proper formatting.
'''

Subtotal = round(float(input("Enter subtotal: $")), 2)
Tip_percent = float(input("Enter tip amount (%): "))

Tip = round(Subtotal * (Tip_percent/100), 2)
Total = round(Subtotal + Tip, 2) #the round function here is actually redundant but just to make sure

print("Subtotal: ${0:0.2f}".format(Subtotal))
print("Tip: ${0:0.2f}".format(Tip))
print("Total: ${0:0.2f}".format(Total))