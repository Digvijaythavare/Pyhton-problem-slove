def showBalance(balance):
    print("****************************")
    print(f"Your Balance is 💲{balance:.2f}")
    print("****************************")

def deposit():
    print("****************************")
    amount = float(input("Enter an amount to be deposited 💲: "))
    print("****************************")
    if amount < 0:
        print("****************************")
        print("That's not a vaild amount")
        print("****************************")
        return 0
    else:
        return amount    

def withdraw(balance):
    print("****************************")
    amount  = float(input("Enter amount to be withdrawn💲: "))
    print("****************************")
    if amount > balance:
        print("****************************")
        print("Insfficient funds")
        print("****************************")
        return 0
    elif amount < 0:
        print("****************************")
        print("Amount must be grater than 0")
        print("****************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_runing = True

    while is_runing:
        print("****************************")
        print("     Banking Program    ") 
        print("****************************")
        print("1.Show Balance 💲")
        print("2.Deposit 💸")
        print("3.withdraw 💶")
        print("4.Exit ❌")
        print("****************************")

        choice = input("Enter your chioce (1-4)❓: ")

        if choice == '1':
            showBalance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_runing = False

        else:
            print("****************************")
            print("That is not a vaild choice❌")   
            print("****************************") 

    print("****************************")
    print("Thank you have a nice day🙏")      
    print("****************************")                      

if __name__ == '__main__':
    main()    