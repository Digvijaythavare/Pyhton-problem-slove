users = {}

def sigup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users:
        print("Username already exists. Please choose a different username.")
    else:
        users[username] = password
        print("Signup successful!")  


sigup()

def signin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Signin successful!")
    else:
        print("Invalid username or password.")