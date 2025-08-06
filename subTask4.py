attendees = []

def get_attendee_info():

    name = input("Please Enter your name: ")

    while True:
        age_type = input("Please enter your age: ")
        if age_type.isdigit():
            age = int(age_type)
            break
        else:
            print("Invalid age. Please enter a number.")

    while True:        
        ticket = input("Please Enter your ticket type (VIP or Regular): ").strip().lower()

        if ticket in ["vip", "regular"]:
            break
        else:
            print("Invalid ticket type. Please enter VIP or Regular.")

    return {
            "name": name,
            "age": age,
            "ticket_type": ticket.upper()
        }

def assign_zone(age, ticket_type):
    if age < 18:
        return "Youth Zone"
    elif ticket_type.upper() == "VIP":
        return "VIP Zone"
    else:
        return "Standard Zone"

def store_attendee(data):
    attendees.append(data)

def print_summary():
    print("Attendees:")
    for attendee in attendees:
        zone = assign_zone(attendee["age"], attendee["ticket"])
        print(f"{attendee['name']} ({attendee['age']} yrs, {attendee['ticket']}): {zone}")


def print_zone_and_age_summary():
    zone_count = {"Youth Zone": 0, "VIP Zone": 0, "Standard Zone": 0}
    total_age = 0

    for attendee in attendees:
        zone = assign_zone(attendee["age"], attendee["ticket"])
        zone_count[zone] += 1
        total_age += attendee["age"]

    total_attendees = len(attendees)
    average_age = total_age / total_attendees if total_attendees > 0 else 0

    print("\n--- Summary Report ---")
    print(f"Total VIP attendees: {zone_counts['VIP Zone']}")
    print(f"Total Youth attendees: {zone_counts['Youth Zone']}")
    print(f"Total Standard attendees: {zone_counts['Standard Zone']}")
    print(f"Average age of attendees: {average_age:.1f}")

while True: 
    attendee = get_attendee_info()
    store_attendee(attendee)
    print("Attendee Registered")

    more = input("Add another attendee? (yes/no): ").strip().lower()
    if more != "yes":
        break

