security_code = input("Enter the security code: ")
department = input("Enter your department: ")
access_level = input("Enter your access level: ")

if security_code == "12345":
    print("Access granted.")

    if department.lower() == "it":
        print("Welcome to the It department.")

        if access_level >= 5:
            print("Welcome to meeting room.")

        else:
            print("Access denied to meeting room.")    
    else:
        print("Access denied to the department.")

else:
    print("Access denied Invalid security code.")     


