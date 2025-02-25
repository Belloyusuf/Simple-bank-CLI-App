import sqlite3
from datetime import datetime 

# balance = 0

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               balance INTEGER NOT NULL,
               created_at TEXT NOT NULL
               )
""")

conn.commit()


# Deposit balance
def deposit():
    # global balance
    try:

        deposit_amount = int(input("Enter the amount you want to deposit: "))
        created_at = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
        if deposit_amount <= 0:
            print("You can't deposit 0 or less")
        else:
            cursor.execute("INSERT INTO customer (balance, created_at) VALUES (?, ?)",(deposit_amount, created_at))
            conn.commit()
            print(f"You deposited {deposit_amount} Successfully")
    except ValueError:
        print("Invalid input, please enter a valid number")

# Withdraw
def withdraw_amount():
    try:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        created_at = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")

        if withdraw <= 0:
            print("Withdrawal balance must be greater then 0")
        
        # Fetch current balance
        cursor.execute("SELECT balance FROM customer WHERE id = 1")
        result = cursor.fetchone()

        if result:
            current_balance = result[0]
       
        if withdraw > current_balance:
            print("Insuffencient Balance")
        else:
            new_balance = current_balance - withdraw
            cursor.execute("UPDATE customer SET balance = ?, created_at = ? WHERE id = 1", new_balance, created_at)
        
            
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
            # elif choice == 2:
            #     withdraw_amount()
            # elif choice == 3:
            #     check_balance()
            # elif choice == 4:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice! Please choose a valid option.")
    print("Thanks for banking with us")



if __name__ =="__main__":
    main_menu()
