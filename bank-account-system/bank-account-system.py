from datetime import datetime

class Bank:
    def __init__(self,name,epassword,balance):
        if not isinstance(name,str):
            raise TypeError("Your name must be of type string.")
        if not isinstance(epassword,int):
            raise TypeError("Your ID must be of type integer.")
        if not isinstance(balance,(float,int)):
            raise TypeError("The balance must be of type float or integer.")
        self.name=name
        self._balance=balance
        password=123456
        if password==epassword:
            print("Password entered correctly")
        else:
            raise ValueError("Password entered incorrectly")
    
    def show_balance(self):
        print(f"balance: ${self._balance:.1f}")
    def dep_money(self):
        amount=float(input("Enter the amount to deposit: "))
        self._balance+=amount
    def with_money(self):
        amount=float(input("Enter the amount to deposit: "))
        if amount>self._balance:
            print("The amount you withdraw cannot exceed your balance.")
        else:
            self._balance-=amount

class Sav_Account(Bank):
    def __init__(self,name,epassword,balance):
        super().__init__(name,epassword,balance)
    
    def interest(self):
        interest_money=float(input("Enter the amount to be deposited into interest: "))
        if interest_money>self._balance:
            print("The amount to be deposited for interest cannot exceed the balance.")
        else: 
            self._balance-=interest_money
            now=datetime.now()
            input_year=str(input("Enter when the interest will end(1 January 2025)e.g.: "))
            interest_year=datetime.strptime(input_year,"%d %B %Y")
            past_day=interest_year-now
            money=(interest_money/100)*(past_day.days/365)*(4)
            print(f"Earned up to {money:.1f}")
            self._balance+=money


a1=Bank("Halil",123456,5000)
a2=Sav_Account("Halil",123456,5000)
