import os 
import re
import json

USER_NAMES="Datas/USER.json"
class USER:
    def __init__(self):
        if not os.path.exists(USER_NAMES):
            with open(USER_NAMES,"w",encoding="utf-8") as f:
                json.dump([],f,ensure_ascii=False,indent=2)

    def read_user(self):
        with open(USER_NAMES,"r",encoding="utf-8") as f:
            return json.load(f)
        
    def save_user(self,user):
        with open(USER_NAMES,"w",encoding="utf-8") as f:
            json.dump(user,f,ensure_ascii=False,indent=2)
    
    def add_user(self):
        name=str(input("Enter your name:"))
        name_space_checker=re.findall(r"\s",name)
        if name_space_checker:
            print("Spaces cannot be used in the name")
        else:
            name_character_checker=re.search(r"\w{4,}",name)
            if not name_character_checker:
                print("The name cannot contain less than 4 characters and no special characters other than _,! .")       
            else:
                users=self.read_user()
                check_user=[item for item in users if item["name"]!=name]
                if len(check_user)==len(users):
                    cclass=str(input("Enter your class(warrior,witcher):"))
                    cclass_checker=re.findall(r"warrior",cclass)
                    cclass_checker2=re.findall(r"witcher",cclass)
                    if not cclass_checker and not cclass_checker2 :
                        print("You entered the wrong class")
                    else:
                        new_user={"name":name,"class":cclass}
                        user=self.read_user()
                        user.append(new_user)
                        self.save_user(user)
                        print(f"{name} has been added!")               
                else:
                    print(f"{name} already exists.")
    
    def delete_user(self):
        name=str(input("Enter the name to delete:"))
        user=self.read_user()
        update_user=[item for item in user if item["name"]!=name]
        if len(update_user)==len(user):
            print(f"{name} not found")
        else:
            self.save_user(update_user)
            print(f"{name} was deleted.")
    
    def all_user_delete(self):
        with open(USER_NAMES,"w",encoding="utf-8") as f:
            f.write("[]")
    
    def show_user(self):
        user=self.read_user()
        if not user:
            print("There are no users listed")
        else:
            for item in user:
                print(f"Name: {item["name"]} - Class: {item["class"]}")

class UserMenu:
    def __init__(self):
        self.manager=USER()
    def run(self):
        while True:
            print("--RPG User Database--")
            print("1- Add user")
            print("2- Delete user")
            print("3- Show all users")
            print("4- Delete all users")
            print("5- Exit")
            choice=int(input("Choose an option:"))
            if choice==1:
                self.manager.add_user()
            elif choice==2:
                self.manager.delete_user()
            elif choice==3:
                self.manager.show_user()
            elif choice==4:
                self.manager.all_user_delete()
            elif choice==5:
                print("Exiting....")
                break
            else:
                print("Invalid option! Please try again!")

u1=UserMenu()
u1.run()

