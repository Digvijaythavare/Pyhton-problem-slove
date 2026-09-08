print("===== FOOD ORDER SYSTEM =====")

print("\nMenu:")
print("1. Pizza      ₹200")
print("2. Burger     ₹120")
print("3. Biryani    ₹180")
print("4. Sandwich   ₹100")

choice = int(input("\nSelect item (1-4): "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Pizza"
    price = 200
elif choice == 2:
    item = "Burger"
    price = 120
elif choice == 3:
    item = "Biryani"
    price = 180
elif choice == 4:
    item = "Sandwich"
    price = 100
else:
    print("Invalid choice!")
    exit()

total = price * quantity

print("\n===== ORDER BILL =====")
print("Item     :", item)
print("Quantity :", quantity)
print("Price    : ₹", price)
print("Total    : ₹", total)
print("======================")
print("Order Placed Successfully!")