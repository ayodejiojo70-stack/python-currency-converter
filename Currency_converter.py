def naira_to_dollar(naira):
    rate = 0.0024  # Example exchange rate: 1 NGN = 0.0024 USD
    return naira * rate

def dollar_to_naira(dollar):
    rate = 415  # Example exchange rate: 1 USD = 415 NGN
    return dollar * rate

def currency_converter():
    print("💰 Welcome to the Currency Converter!")
    print("1: Naira to Dollar")
    print("2: Dollar to Naira")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        try:
            naira = float(input("Enter amount in Naira: "))
            print(f"{naira} NGN = ${naira_to_dollar(naira):.2f} USD")
        except ValueError:
            print("⚠️ Please enter a valid number.")
    elif choice == "2":
        try:
            dollar = float(input("Enter amount in Dollars: "))
            print(f"${dollar} USD = {dollar_to_naira(dollar):.2f} NGN")
        except ValueError:
            print("⚠️ Please enter a valid number.")
    else:
        print("⚠️ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    currency_converter()
