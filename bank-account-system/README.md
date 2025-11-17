# 🏦 Bank Account System

A simple OOP-based banking system that includes password verification, balance display, deposits, withdrawals, and a savings account with daily interest calculation.

This project demonstrates object-oriented programming concepts such as:

Class inheritance

Data encapsulation (_balance)

Error handling

Input validation

Date-based calculations

# # 🚀 Features
🔸 Bank Class

Password-protected account creation

Display balance

Deposit money

Withdraw money

🔸 Savings Account (Sav_Account)

Inherits everything from Bank

Ability to invest part of the balance into interest

Calculates earned interest based on real calendar days

Adds earned interest back into balance

# # 📘 Available Methods
# # # 🏦 Bank Class Methods
Method	Parameters	Description:
show_balance()	—	Shows the current account balance
dep_money()	User input	Deposits money into the account
with_money()	User input	Withdraws money from the account
__init__(name, epassword, balance)	name: str, epassword: int, balance: float/int	Creates a protected bank account

# # # 💰 Sav_Account Class Methods
Method	Parameters	Description:
interest()	User input	Deposits money into interest, calculates earnings, and adds profit to balance
Inherits show_balance()	—	Shows balance
Inherits dep_money()	User input	Deposit money
Inherits with_money()	User input	Withdraw money
Inherits __init__()	same as Bank	Creates savings account
