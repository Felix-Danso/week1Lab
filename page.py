name = input("Please Enter your name: ")
while True:
    age_type = input("Please enter your age: ")
    if age_type.isdigit():
        age = int(age_type)
        break
    else:
        print("Invalid age. Please enter a number.")
ticket_type = input("Please Enter your ticket type (VIP or Regular): ")

ticket_type = ticket_type.strip().lower()

if ticket_type == "vip" or ticket_type == "regular":
    attendee = {
        "name": name,
        "age": age,
        "ticket_type": ticket_type.upper()
    }

    print("Attendee Registered")
else:
    print("Invalid ticket type. Please enter VIP or Regular.")

