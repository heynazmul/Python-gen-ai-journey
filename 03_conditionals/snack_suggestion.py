"""
This program is for a local cafe.
It takes snack input from the customer.
If the snack is 'cookies' or 'samosa', it confirms the order.
Otherwise, it shows that the item is not available.
"""


snack = input("Enter Your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! we'll serve you {snack} is confirmed ✅")
else:
    print("sorry, we only serve cookies or samosa with tea ❌")