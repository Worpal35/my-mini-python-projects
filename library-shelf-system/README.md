# 📚 Bookshelf Manager

A simple and clean **Object-Oriented Python project** that simulates a virtual bookshelf system. You can create shelves, add books, remove books, check their existence, and display all stored books — all using an OOP-based structure.

---

# 🚀 Features

* Create shelves with custom names
* Create books with title, author, and page count
* Add books to shelves
* Remove books from shelves
* Display all books stored in a shelf
* Check if a specific book exists on a shelf
* Fully Object-Oriented structure using **classes and objects**

---

# 🧩 Class Structure

## 🗄️ **Shelf Class**

Manages a list of books.

### Methods:

| Method                 | Description                          |
| ---------------------- | ------------------------------------ |
| `add_book(book)`       | Adds a book to the shelf             |
| `del_book(book_title)` | Removes a book by title              |
| `show_library()`       | Displays all books in the shelf      |
| `on_shelf(book_title)` | Checks if a book exists on the shelf |

---

## 📖 **Book Class**

Represents a single book.

### Attributes:

* `title` — Title of the book
* `author` — Author name
* `page` — Number of pages

### Methods:

| Method        | Description                              |
| ------------- | ---------------------------------------- |
| `show_book()` | Prints the title, author, and page count |

---

# 📂 File Structure

```
library-shelf-system/
├── library-shelf-system.py
```

---

# ▶️ How to Run

```bash
python library-shelf-system.py
```

Follow the menu instructions or modify the script to test the classes.

---

# 📜 License

This project uses the MIT License.
