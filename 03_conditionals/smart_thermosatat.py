"""
You're building a smart thermostat alert system:
If the device_status is "active"
And temperature > 35 → Warn: "High temperature alert!"
Else: "Temperature normal"
If device is off "Device is offline
"""

device_status = "active"

temprature = 37

if device_status == "active":
    if temprature >35:
        print("High temperature alart! 🔥")
    else:
        print("Tempreature is normal  😊")
else: 
    print("Device is offline")