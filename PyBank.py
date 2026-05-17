# ============================================================
#  🏦  BANK ACCOUNT SYSTEM
#  Concepts used: Classes, Inheritance, Loops, Error Handling
# ============================================================

# ── PARENT CLASS ────────────────────────────────────────────
# Think of this like a "blueprint" for any Person.
# It stores basic info every person has: name and age.

class Person:
    def __init__(self, name: str, age: int):
        # Validate name — cannot be empty or just spaces
        if not name.strip():
            raise ValueError("❌ Name cannot be empty.")

        # Validate age — must be a positive number
        if age <= 0:
            raise ValueError("❌ Age must be a positive number.")

        self.name = name.strip().title()   # e.g. "ali raza" → "Ali Raza"
        self.age  = age

    def get_info(self) -> str:
        """Return a neat string with the person's details."""
        return f"👤 Name : {self.name}\n   Age  : {self.age}"


# ── CHILD CLASS ─────────────────────────────────────────────
# BankAccount INHERITS from Person.
# Analogy: Person is a plain notebook; BankAccount is the
# same notebook but with an extra "Money" section added.

class BankAccount(Person):
    def __init__(self, name: str, age: int, initial_balance: float = 0.0):
        # Call the parent (Person) constructor first
        super().__init__(name, age)

        # Validate starting balance
        if initial_balance < 0:
            raise ValueError("❌ Initial balance cannot be negative.")

        self.__balance = initial_balance   # __ means PRIVATE (hidden from outside)

    # ── DEPOSIT ──────────────────────────────────────────────
    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("❌ Deposit amount must be greater than zero.")

        self.__balance += amount
        print(f"\n  ✅ PKR {amount:,.2f} deposited successfully!")
        print(f"  💰 New Balance : PKR {self.__balance:,.2f}")

    # ── WITHDRAW ─────────────────────────────────────────────
    def withdraw(self, amount: float) -> None:
        """Remove money from the account (if enough funds exist)."""
        if amount <= 0:
            raise ValueError("❌ Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError(
                f"❌ Insufficient funds!\n"
                f"   You tried to withdraw : PKR {amount:,.2f}\n"
                f"   Available balance     : PKR {self.__balance:,.2f}"
            )

        self.__balance -= amount
        print(f"\n  ✅ PKR {amount:,.2f} withdrawn successfully!")
        print(f"  💰 Remaining Balance : PKR {self.__balance:,.2f}")

    # ── CHECK BALANCE ─────────────────────────────────────────
    def check_balance(self) -> None:
        """Display current balance."""
        print(f"\n  💰 Current Balance : PKR {self.__balance:,.2f}")

    # ── ACCOUNT SUMMARY ───────────────────────────────────────
    def account_summary(self) -> None:
        """Print all account details in one place."""
        print("\n" + "─" * 40)
        print("  📋  ACCOUNT SUMMARY")
        print("─" * 40)
        print(f"  {self.get_info()}")
        print(f"  💰 Balance : PKR {self.__balance:,.2f}")
        print("─" * 40)


# ── HELPER: safe number input ────────────────────────────────
def get_amount(prompt: str) -> float:
    """Keep asking until the user gives a valid number."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  ⚠️  Please enter a valid number (e.g. 5000).")


# ── MAIN PROGRAM ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("    🏦  WELCOME TO PyBank  🏦")
    print("=" * 50)

    # ── Step 1: Create the account ────────────────────────────
    print("\n  Let's set up your account!\n")

    # Keep asking until valid name is given
    while True:
        try:
            name = input("  Enter your full name : ")
            age  = int(input("  Enter your age       : "))
            bal  = get_amount("  Enter opening balance (PKR) : ")
            account = BankAccount(name, age, bal)
            break
        except ValueError as e:
            print(f"\n  {e}\n  Please try again.\n")

    account.account_summary()

    # ── Step 2: Menu Loop ─────────────────────────────────────
    # This loop keeps running until the user chooses to exit.
    # Analogy: Like an ATM screen that stays on until you press "Exit".

    while True:
        print("\n" + "─" * 40)
        print("  📌  MAIN MENU")
        print("─" * 40)
        print("  [1] 💵 Deposit Money")
        print("  [2] 💸 Withdraw Money")
        print("  [3] 💰 Check Balance")
        print("  [4] 📋 Account Summary")
        print("  [5] 🚪 Exit")
        print("─" * 40)

        choice = input("  Choose an option (1-5) : ").strip()

        if choice == "1":
            # ── Deposit ──────────────────────────────────────
            try:
                amount = get_amount("\n  Enter deposit amount (PKR) : ")
                account.deposit(amount)
            except ValueError as e:
                print(f"\n  {e}")

        elif choice == "2":
            # ── Withdraw ─────────────────────────────────────
            try:
                amount = get_amount("\n  Enter withdrawal amount (PKR) : ")
                account.withdraw(amount)
            except ValueError as e:
                print(f"\n  {e}")

        elif choice == "3":
            # ── Check Balance ─────────────────────────────────
            account.check_balance()

        elif choice == "4":
            # ── Full Summary ──────────────────────────────────
            account.account_summary()

        elif choice == "5":
            # ── Exit ──────────────────────────────────────────
            print(f"\n  👋 Goodbye, {account.name}! Thank you for using PyBank.")
            print("=" * 50)
            break

        else:
            print("\n  ⚠️  Invalid choice. Please enter a number between 1 and 5.")


# ── Entry Point ───────────────────────────────────────────────
# This means: "Only run main() if this file is executed directly."
# (Not when it is imported by another file.)
if __name__ == "__main__":
    main()