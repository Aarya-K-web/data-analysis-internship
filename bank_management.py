"""Menu-driven bank account manager."""

from datetime import datetime


def get_positive_amount(prompt):
    """Return a positive monetary amount entered by the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid input. Enter a numeric amount (for example, 250.50).")


def record_transaction(history, transaction_type, amount, balance):
    """Store one completed account transaction."""
    history.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "amount": amount,
        "balance": balance,
    })


def deposit(balance, history):
    amount = get_positive_amount("Enter deposit amount: Rs. ")
    balance += amount
    record_transaction(history, "Deposit", amount, balance)
    print(f"Deposit successful. New balance: Rs. {balance:,.2f}")
    return balance


def withdraw(balance, history):
    amount = get_positive_amount("Enter withdrawal amount: Rs. ")
    if amount > balance:
        print("Insufficient balance. Withdrawal cancelled.")
        return balance

    balance -= amount
    record_transaction(history, "Withdrawal", amount, balance)
    print(f"Withdrawal successful. New balance: Rs. {balance:,.2f}")
    return balance


def check_balance(balance):
    print(f"Current balance: Rs. {balance:,.2f}")


def show_transaction_history(history):
    if not history:
        print("No transactions have been made yet.")
        return

    print("\nTransaction History")
    print("-" * 72)
    print(f"{'Date and Time':<21}{'Type':<15}{'Amount':>18}{'Balance':>21}")
    print("-" * 72)
    for transaction in history:
        print(
            f"{transaction['time']:<21}{transaction['type']:<15}"
            f"{'Rs. ' + format(transaction['amount'], ',.2f'):>18}"
            f"{'Rs. ' + format(transaction['balance'], ',.2f'):>21}"
        )


def display_menu():
    print("\n--- Bank Management System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")


def main():
    balance = 0.0
    history = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            balance = deposit(balance, history)
        elif choice == "2":
            balance = withdraw(balance, history)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            show_transaction_history(history)
        elif choice == "5":
            print("Thank you for using the Bank Management System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()


# Code review notes:
# - Use Decimal instead of float for currency to avoid precision errors.
# - Add type hints and model transactions with a dataclass rather than dictionaries.
# - Store datetime objects and format them only when displaying transaction history.
# - Separate user input/output from deposit and withdrawal business logic for easier testing.
# - Handle EOFError and KeyboardInterrupt for graceful program termination.
