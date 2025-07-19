class ATM:
    def __init__(self,balance=0):
        self.balance=balance
        self.pin="1234" #Default PIN
    def authenticate(self):
        attempts=3
        while attempts>0:
            user_pin=input("Enter your 4-digit PIN:")
            if user_pin==self.pin:
                print("Authentication successful!\n")
                return True
            else:
                                attempts-=1
                                print(f"Incorrect PIN.{attempts} attempt(s) left.\n")
        print("Too many incorrect attempts.Access blocked.")
        return false
    def display_menu(self):
        print("\n------ATM Menu------")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Change PIN")
        print("5.Exit")
    def check_balance(self):
        print(f"\n Current balance:₹{self.balance:.2f}\n")
    def deposit(self):
        try:
            amount=float(input("Enter amount to deposit:₹"))
            if amount<=0:
                print("Amount must be positive.\n")
            else:
                self.balance+=amount
                print(f"₹{amount:.2f} deposited successfuly.\n")
        except ValueError:
            print("Invalid input.Please enter a valid number.\n")
    def withdraw(self):
        try:
            amount=float(input("Enter amount to withdraw:₹"))
            if amount<=0:
                print("Amount must be positive.\n")
            elif amount>self.balance:
                print("Insufficient balance.\n")
            else:
                self.balance-=amount
                print(f"₹{amount:.2f} withdrawn successfully.\n")
        except ValueError:
            print("Invalid input.Please enter a valid number.\n")
    def change_pin(self):
        current_pin=input("Enter current PIN:")
        if current_pin==self.pin:
            new_pin=input("Enter new 4-digit PIN:")
            confirm_pin=input("Re-enter new PIN to confirm:")
            if new_pin==confirm_pin and len(new_pin)==4 and new_pin.isdigit():
                self.pin=new_pin
                print("PIN changed successfully!\n")
            else:
                print("PINs do not match or are invalid.PIN not changed.\n")
        else:
            print("Incorrect current PIN.\n")
    def run(self):
        if not self.authenticate():
            return
        while True:
            self.display_menu()
            choice=input("Choose an option(1-5):")
            if choice=='1':
                self.check_balance()
            elif choice=='2':
                self.deposit()
            elif choice=='3':
                self.withdraw()
            elif choice=='4':
                self.change_pin()
            elif choice=='5':
                print("Thank you for using the ATM.Goodbye!\n")
                break
            else:
                print("Invalid selection.Please try again.\n")
atm=ATM(balance=1000) #Set starting balance
atm.run()
