import datetime

# Functions
from withdrawal import withdraw
from deposit import deposit
from loading import load

# Global Variables
balance = 3000
withdrawal_limit = 3
extract = ""

menu = " Bank System ".center(28, "*")
current_hour = datetime.datetime.now().strftime("%H:%M:%S")

#Conditions
while True:
    option = int(input(f"""
{menu}

[1] Withdraw
[2] Deposit
[3] Extract
[4] Exit

{menu}
"""))
    
    if option == 1 :
        value = float(input(f"balance: {balance:.2f}\nEnter the value: "))
        balance, extract, withdrawal_limit = withdraw(balance, withdrawal_limit, extract, value, current_hour)
        load()

    elif option == 2:
        value = float(input(f"balance: {balance:.2f}\nEnter the value: "))
        balance, extract = deposit(balance, extract, value, current_hour)
        load()

    elif option == 3:
        print("No movements were made" if not extract else extract)
        print(f"\nBalance: R$ {balance:.2f}")
        load()

    else:
        print("Thank you for using our System!")
        break