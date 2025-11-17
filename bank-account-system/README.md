# 🏦 Bank Account System

A simple **OOP-based banking system** that includes password verification, balance management, deposits, withdrawals, and a savings account that earns daily interest.

This project demonstrates fundamental object-oriented programming concepts such as:

* **Class inheritance**
* **Data encapsulation** (`_balance`)
* **Error handling**
* **Input validation**
* **Date-based interest calculation**

---

# 🚀 Features

## 🔹 Bank Class

* Password-protected account creation
* Display balance
* Deposit money
* Withdraw money

## 🔹 Savings Account (`Sav_Account`)

* Inherits all features of `Bank`
* Allows investing part of the balance into interest
* Calculates earned interest based on real calendar days
* Automatically adds earned interest back into the main balance

---

# 📘 Available Methods

## 🏦 **Bank Class Methods**

| Method                               | Parameters                                          | Description                      |
| ------------------------------------ | --------------------------------------------------- | -------------------------------- |
| `show_balance()`                     | —                                                   | Displays the current balance     |
| `dep_money()`                        | user input                                          | Deposits money into the account  |
| `with_money()`                       | user input                                          | Withdraws money from the account |
| `__init__(name, epassword, balance)` | `name: str`, `epassword: int`, `balance: float/int` | Creates a protected bank account |

---

## 💰 **Sav_Account Class Methods**

| Method           | Parameters   | Description                                                                    |
| ---------------- | ------------ | ------------------------------------------------------------------------------ |
| `interest()`     | user input   | Deposits money into interest, calculates profit, and adds it back into balance |
| `show_balance()` | —            | *(Inherited)* Shows current balance                                            |
| `dep_money()`    | user input   | *(Inherited)* Deposit money                                                    |
| `with_money()`   | user input   | *(Inherited)* Withdraw money                                                   |
| `__init__()`     | same as Bank | *(Inherited)* Creates a savings account                                        |

---

# 📂 File Structure

```
bank-account-system/
└── main.py
```

# ▶️ How to Run

```bash
python main.py
```

Follow the on-screen instructions.

---

# 📜 License

This project uses the MIT License.
