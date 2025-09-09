"""
You're building a ticket info system for a railway app. Based on seat type, show its features.
Task:
Input: "sleeper" "AC" "general",
"luxury"
Match using match-case
Unknown → show: "Invalid seat type"
"""

seat_type = input("Enter Seat type (sleeper/ac/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No ac, beds available")
    case "ac":
        print("Ac - Air conditioned, comfy ride ")
    case "general":
        print("General - No ac, non bed")  
    case "luxury":
        print("Luxury - Air conditioned, beds, tv, wifi")
    case _:
        print("invalid seat type")
        