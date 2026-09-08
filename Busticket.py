print("===== BUS TICKET BOOKING =====")

name = input("Passenger Name: ")
age = int(input("Age: "))

print("\nAvailable Buses:")
print("1. Pune -> Mumbai  ₹500")
print("2. Pune -> Nashik  ₹400")
print("3. Pune -> Goa     ₹1200")

choice = int(input("\nSelect Bus (1-3): "))
seats = int(input("Number of Seats: "))

if choice == 1:
    bus = "Pune -> Mumbai"
    price = 500
elif choice == 2:
    bus = "Pune -> Nashik"
    price = 400
elif choice == 3:
    bus = "Pune -> Goa"
    price = 1200
else:
    print("Invalid bus choice!")
    exit()

total = price * seats

print("\n===== TICKET =====")
print("Passenger :", name)
print("Age       :", age)
print("Bus       :", bus)
print("Seats     :", seats)
print("Price     :", price)
print("Total     :", total)
print("==================")
print("Booking Successful!")