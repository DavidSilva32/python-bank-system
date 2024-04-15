def withdraw(balance, extract, withdrawal_limit, value, current_hour):
    LIMIT_BY_WITHDRAWAL = 500

    if (value <= LIMIT_BY_WITHDRAWAL) and (withdrawal_limit > 0) and (balance >= value) and (value >= 0):
        withdrawal_limit -= 1
        balance -= value
        extract += f"Withdrawal: R$ {value:.2f} {current_hour}\n"
        print("Withdraw successfully!")
        return balance, extract, withdrawal_limit

    elif value > LIMIT_BY_WITHDRAWAL:
        print(f"The value: {value} is bigger than limit by withdrawal: {LIMIT_BY_WITHDRAWAL}")
        return balance, extract, withdrawal_limit
    
    elif withdrawal_limit == 0:
        print("Withdrawal limit reached. You cannot make any more withdrawals.")
        return balance, extract, withdrawal_limit
    
    elif balance < value:
        print("Insufficient balance for withdrawal.")
        return balance, extract, withdrawal_limit
    
    else:
        print("Invalid value!")
        return balance, extract, withdrawal_limit