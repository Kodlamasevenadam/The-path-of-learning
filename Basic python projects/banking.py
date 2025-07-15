# Python banking program

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Deposit amount must be positive.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw:"))

    if amount > balance:
        print("Insufficient funds. Cannot withdraw that amount.")
        return 0
    elif amount < 0:
        print("Withdrawal amount must be positive.")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Please choose an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("Thank you for using the banking program. Goodbye!")
            is_running = False
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
