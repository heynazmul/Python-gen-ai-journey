
"""
A tea stall offers different prices for different cup sizes. Write a program that calculates the price based on size.
Task:
Input: "small", "medium", "large"
Small → 10, Medium → ₹15, Large → ₹20
If invalid: show "Unknown cup size"
"""

cup = input("Chose your cup size (small/midium/large): ").lower()

if cup == "small":
    print("Price is 10 taka")
elif cup == "medium":
    print("Price is 15 taka")
elif cup == "large":
    print("prize is 20 taka")
else:
    print ("Unknown Cup size")