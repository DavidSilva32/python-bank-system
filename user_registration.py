def filter_user(users: list, cpf: str):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    print(filtered_users)
    return filtered_users[0] if filtered_users else None

def register_user(users: list): # users = [{"name": "Nathan", "bith": "07/09/1993", "cpf": 18758740302, "address": "alameda irineia verçosa,18 - campo lindo - seropedica/RJ"}]
    CPF = input("Enter your CPF (Only numbers): ")
    user = filter_user(users, CPF)

    if user:
        return print("User already registered!")

    name = input("Enter your name: ").title()
    bith_date = input("Enter your date of birth (mm-dd-yyyy): ")
    address = input("Enter your address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "bith_date": bith_date, "cpf": CPF, "address": address})

    print(f"\nUser created successfully!")

def creat_account(users: list, number_account: int, agency: str):
    CPF = input("Enter your CPF (Only numbers): ")
    user = filter_user(users, CPF)

    if user:
        print("\nACcount created successfully!")
        return {"agency": agency, "number_account": number_account, "user": user}
    
    print("\nUser not found!")