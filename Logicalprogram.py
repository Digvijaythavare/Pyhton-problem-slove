print("....This is a logical program example...")


Customer_name = input("Enter the customer name: ")
Customer_age = int(input("Enter the customer age: "))
Customer_gender = input("Enter the customer gender: ")
Customer_Id = int(input("Enter the customer ID: "))


if Customer_age >= 18:
    print(f"Customer Name: {Customer_name}")
    print(f"Customer Age: {Customer_age}")
    print(f"Customer Gender: {Customer_gender}")
    print(f"Customer ID: {Customer_Id}")
    print("Customer is eligible to buy a car.")

elif Customer_age < 18:
    print(f"Customer Name: {Customer_name}")
    print(f"Customer Age: {Customer_age}")
    print(f"Customer Gender: {Customer_gender}")
    print(f"Customer ID: {Customer_Id}")
    print("Customer is not eligible to buy a car.")

elif Customer_age == 18:
    print(f"Customer Name: {Customer_name}")
    print(f"Customer Age: {Customer_age}")
    print(f"Customer Gender: {Customer_gender}")
    print(f"Customer ID: {Customer_Id}")
    print("Customer is eligible to buy a car.")

else:
    print("Invalid age entered.")