import re

password=input("Enter the password: ")

uncorrect=re.findall(r"\s",password)
searching=re.findall(r"[A-Za-z0-9^!@#$%^&*_?]{6,}",password)

if uncorrect:
    print("There cannot be any spaces in the password.")
else:    
    if searching:
        print(f"Your password({password}) is strong.")
    else:
        print(f"Your password({password}) is weak. ")