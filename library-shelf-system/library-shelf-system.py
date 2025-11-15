class Shelf:
    def __init__(self,lname):
        if not isinstance(lname,str):
            raise TypeError("The shelf name must be of type string.")
        self.lname=lname
        self.libarys_book=[]
    
    def add_book(self,addbook):
        self.libarys_book.append(addbook)
    
    def del_book(self,delbook):
        self.libarys_book.remove(delbook)
    
    def show_libary(self):
        print(f"Shelf : {self.lname}")
        for item in self.libarys_book: 
            print(f"{item.title}({item.author}): {item.pagenumber} page.")
    
    def on_self(self):
        search_title = str(input("Enter book name: ")).strip()
        
        found = False        
        for book in self.libarys_book:
            if book.title.lower() == search_title.lower():
                print(f"Yes, the book {search_title} is on this shelf ({self.lname}).")
                found = True
                break
        if not found:
            print(f"The book {search_title} is not on this shelf ({self.lname}).")


class Book(Shelf):
    def __init__(self,title,author,pagen):
        if not isinstance(title,str):
            raise TypeError("The title must be of type string.")
        if not isinstance(author,str):
            raise TypeError("The author name must be of type string.")
        if not isinstance(pagen,int):
            raise TypeError("Page number must be integer type.")
        self.title=title
        self.author=author
        self.pagenumber=pagen
        
    def show_book(self):
        print(f"{self.title}({self.author}): {self.pagenumber} page")

s1=Shelf("1st shelf of the library")
s2=Shelf("2nd shelf of the library")
b1=Book("1984","George Orwell",328)
b2=Book("The Hunger Games","Suzanne Collins",374)
b3=Book("To Kill a Mockingbird","Harper Lee",323)

#FOR EXAMPLE
# s1.add_book(b1)
# s1.add_book(b2)
# s1.show_libary()
# s1.del_book(b1)
# s1.show_libary()

# s1.on_self()

# b1.show_book()
