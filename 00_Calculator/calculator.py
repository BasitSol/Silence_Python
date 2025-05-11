print("Welcome to the SAFE CALCULATOR WORLD")


def add(num1 ,num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        return num1 / num2
    except:
        return "Error: Cannot divide by zero."

def expo(num1, num2):
    return num1**num2

def floor(num1, num2):
    try:
        return num1 // num2
    except:
        return "Error: Cannot floor divide by zero."

try:
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
except:
    print("Invalid input. Please enter Inbteger Value only).")
    exit()

while True:
    print("Enter Your Operation,")
    print("1: for the ADD(+):")
    print("2: for the Subtract(-):")
    print("3: for the Mulitply(*):")
    print("4: for the Division(/):")
    print("5: for the Exponent(**):")
    print("6: for the Floor Operation(//):")
    print("7: for the EXIT:")

    choice = input("Enter Your Choice:")

    if choice == '1':
        result = add(num1, num2)
        print("Your Result is:",result)
        with open("historyofCalc.txt", "a") as file: 
           file.write(f"{num1} + {num2} = {result}\n")

    elif choice == '2':
        result = subtract(num1, num2)
        print("Your Result is :", result)
        with open("historyofCalc.txt", "a") as file: 
           file.write(f"{num1} - {num2} = {result}\n")

    elif choice == '3':
        result = multiply(num1, num2)
        print("Your Result is :", result)
        with open("historyofCalc.txt", "a") as file: 
           file.write(f"{num1} * {num2} = {result}\n")
           
    elif choice == '4':
        result = division(num1, num2)
        print("Your Result is:", result)
        with open("historyofCalc.txt", "a") as file: 
           file.write(f"{num1} / {num2} = {result}\n")
    elif choice == '5':
        result = expo(num1, num2)
        print("Your Result is :", result)
        with open("historyofCalc.txt", "a") as file: 
           file.write(f"{num1} ** {num2} = {result}\n")
    elif choice == '6':
        result = floor(num1, num2)
        print("Your Result is:", result)
        with open("historyofCalc.txt", "a") as file: 
            file.write(f"{num1} // {num2} = {result}\n")
    elif choice == '7':
        break
    else:
        print("PLease Enter the Valid Choice !")