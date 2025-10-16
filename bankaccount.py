class bankaccount:                   #class,obj

    def __init__(self, initial_balance=0.0):
        self.__balance = initial_balance           #encaps (private)
        print(f"Account created with initial balance: ${self.__balance:.2f}")

    def show_balance(self):
        print("****************************")
        print(f"Your balance is ${self.__balance:.2f}")
        print("****************************")

    def deposit(self):
        print("***********************************")
        try:
            amount = float(input("Enter an amount to be deposited: "))
        except ValueError:
            print("Invalid input.")
            return

        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount:.2f} successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        print("***********************************")
        try:
            amount = float(input("Enter amount to be withdrawn: "))
        except ValueError:
            print("Invalid input.")
            return

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful.")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"Account Status (Base): Balance=${self.__balance:.2f}"
