name = input("Please Enter your name: ")
while True:
    age_type = input("Please enter your age: ")
    if age_type.isdigit():
        age = int(age_type)
        break
    else:
        print("Invalid age. Please enter a number.")
ticket_type = input("Please Enter your ticket type (VIP or Regular): ").strip().lower()

if age < 18:
    zone = "Youth Zone"
elif ticket_type == "vip":
    zone = "VIP Zone"
elif age >= 18 and ticket_type == "regular":
    zone = "Standard Zone"
else:
    zone = "unknown Zone"

print("You have been placed in the", zone)
