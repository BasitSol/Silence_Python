# this is the simple ATM Calculator
balance = 1000

while True:
    print("\n Welcome to the ATM Machine")
    print("\n 1. To check Balance: ")
    print("\n 2. To Deposit Money: ")
    print("\n 1. To Withdraw Money: ")
    print("\n 1. To Exit: ")

    choice = input("Enter the Choice (1 - 4)")

    if choice == '1':
        print(f"Your Balance is: ${balance}")
    
    elif choice == '2':
        deposit = float(input("Enter the Amount: $"))
        balance += deposit
        print(f"Now you Current Balance is ${deposit}")

    elif choice == '3':
        withdraw = float(input("Enter the amount which you want to withdraw: $"))
        if withdraw > balance:
            print("Insufficent Balance")
        else:
           balance -= withdraw
           print(f"Now your Current Balance After Withdrawl is: $ ${balance}")

    elif choice == '4':
        print("You are Exit From ATM Machine")
        break

else:
    print("Invalid Choice! Please try Again !")
