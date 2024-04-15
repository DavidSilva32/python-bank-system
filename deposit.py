def deposit(balance, extract, value, current_hour):
    if value > 0:
        balance += value
        extract += f"Deposit: R$ {value:.2f} {current_hour}\n"
        print("Sucessful deposit!")
        return balance, extract
    
    else:
        print("Invalid value!")
        return balance, extract