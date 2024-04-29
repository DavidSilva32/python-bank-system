import datetime

# Functions
from bank import withdraw, deposit, print_extract
from menu import print_menu
from loading import load
from user_registration import register_user, creat_account

# Global Variables
balance, withdrawal_limit = 3000.00, 3
users, accounts = [], []
extract = ""
AGENCY = "0001"

current_hour = datetime.datetime.now().strftime("%H:%M:%S")

#Conditions
while True:
    option = print_menu()
    
    if option == 1 : # Withdrawal
        value = float(input(f"balance: {balance:.2f}\nEnter the value: "))
        balance, extract, withdrawal_limit = withdraw(balance=balance, withdrawal_limit=withdrawal_limit, extract=extract, value=value, current_hour=current_hour)
        load()

    elif option == 2: # Deposit
        value = float(input(f"balance: {balance:.2f}\nEnter the value: "))
        balance, extract = deposit(balance, extract, value, current_hour)
        load()

    elif option == 3: # Print extract
        print_extract(balance, extract=extract)
        load()

    elif option == 4: # Creat account
        number_account = len(accounts) + 1
        creat_account(users=users, number_account=number_account, agency=AGENCY)
        load()

    elif option == 5: # Register user
        register_user(users)
        load()

    else:
        print("Thank you for using our System!")
        break