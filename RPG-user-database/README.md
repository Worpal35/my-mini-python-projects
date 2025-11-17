# RPG User Database

This project is a simple **RPG Game User Data Management System** written in Python. It allows you to **add**, **delete**, **list**, and **reset** users for an RPG-style game. User data is saved in a JSON file.

## 📌 Features

* Add new users with validation
* Prevent duplicate usernames
* Delete individual users
* Delete all users at once
* Show all saved users
* Automatic creation of JSON data file if it doesn't exist

## 📂 File Structure

```
project-folder/
│
├── main.py                 # Main program
├── Datas/
│   └── USER.json           # Automatically created user database
└── README.md               # Documentation
```

## 🧠 How It Works

User data is stored in `Datas/USER.json` in list format:

```json
[
  {
    "name": "john",
    "class": "warrior"
  }
]
```

The program includes:

* **Input validation** for name and class
* Only allows two classes: `warrior` or `witcher`

## ▶️ How to Run

1. Make sure Python is installed.
2. Create a folder named `Datas` in the same directory.
3. Save the script as `main.py`.
4. Run this command:

   ```bash
   python main.py
   ```

## 📝 Example Menu

```
--RPG Game User Data System--
1- Add user
2- Delete user
3- Show all users
4- Delete all users
5- Exit
```

## 📜 License

If you want to add a license, you can include an **MIT License** or any license of your choice.

## 🏷️ Project Name

**RPG User Data System**
