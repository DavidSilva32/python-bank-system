def print_menu():
    title = " Bank System ".center(28, "*")

    menu = f"""
        {title}

        [1] Withdraw
        [2] Deposit
        [3] Extract
        [4] Creat account
        [5] Register user
        [6] Exit

        {title}
    """
    return int(input(menu))