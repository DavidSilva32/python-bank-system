def withdraw(*, balance: float, extract: str, withdrawal_limit: int, value: float, current_hour: str):
    LIMIT_BY_WITHDRAWAL = 500

    if value > LIMIT_BY_WITHDRAWAL:
        print(f"The value: {value} is bigger than limit by withdrawal: {LIMIT_BY_WITHDRAWAL}")
        return balance, extract, withdrawal_limit
    
    elif withdrawal_limit == 0:
        print("Withdrawal limit reached. You cannot make any more withdrawals.")
        return balance, extract, withdrawal_limit
    
    elif balance < value:
        print("Insufficient balance for withdrawal.")
        return balance, extract, withdrawal_limit

    elif (value >= 0):
        withdrawal_limit -= 1
        balance -= value
        extract += f"Withdrawal:\t\tR${value:.2f} {current_hour}\n"
        print("Withdraw successfully!")
        return balance, extract, withdrawal_limit
    
    else:
        print("Invalid value!")
        return balance, extract, withdrawal_limit
    
def deposit(balance: float, extract: str, value: float, current_hour: str, /):
    if value > 0:
        balance += value
        extract += f"Deposit:\t\tR${value:.2f} {current_hour}\n"
        print("Sucessful deposit!")
        return balance, extract
    
    else:
        print("Invalid value!")
        return balance, extract
    
def print_extract(balance: float, /, *, extract: str):
    print("No movements were made" if not extract else extract)
    print(f"\nBalance:\t\tR${balance:.2f}")