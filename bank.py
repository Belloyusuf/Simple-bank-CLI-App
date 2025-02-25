
balance = 0

# Deposit balance
def deposit():
    global balance
    try:
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        if deposit_amount <= 0:
            print("You can't deposit 0 or less")
        else:
            balance += deposit_amount
            print(f"You deposited {deposit_amount} Successfully")
    except ValueError:
        print("Invalid input, please enter a valid number")

# Withdraw
def withdraw_amount():
    global balance
    try:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw <= 0:
            print("Withdrawal balance must be greater then 0")
        elif withdraw > balance:
            print("Insufficent Balance")
        else:
            balance -= withdraw
            print(f"You withdrew ${withdraw} successfully")
    except ValueError:
        print("Invalid input, please enter a valid number")

# check balance
def check_balance():
    print(f"Your Account Balance is ${balance}")


def menu():
    print("\n *** My Bank *** ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("")

# Main menu of the program
def main_menu():
    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw_amount()
            elif choice == 3:
                check_balance()
            elif choice == 4:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice! Please choose a valid option.")
    print("Thanks for banking with us")



if __name__ =="__main__":
    main_menu()
