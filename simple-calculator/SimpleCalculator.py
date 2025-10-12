import math
while True:
    print("=== Simple Calculator ===")
    transactions=["Add","Subtract","Multiply","Divide","Factorial","GCD","LCM","Remaining from Divide","Exponential"]
    sort= range(1,len(transactions)+1)
    for transactions,sort in zip(transactions,sort):
        print(f"{sort}-{transactions}")

    choose = int(input("Select action (1-10): "))
    isCorrect=1
    if choose<1 or choose>10:
        print("Please make the right choice")
        isCorrect=0

    if choose==5:
        isCorrect=2
    if choose==9:
        isCorrect=3
    if choose==6 or choose==7:
        isCorrect=4

    if isCorrect == 1:
            number1=float(input("Enter first number: "))
            number2=float(input("Enter second number: "))
            if choose==1:
                result=number1+number2
                print("Result:",result)
            elif choose==2:
                result=number1-number2
                print("Result:",result)
            elif choose==3:
                result=number1*number2
                print("Result:",result)
            elif choose==4:
                result=number1/number2
                print("Result:",result)
            elif choose==8:
                result=number1%number2
                print("Result:",result)

    if isCorrect == 2:
        number=int(input("Enter number: "))
        result=math.factorial(number)
        print(result)

    if isCorrect == 3:
        number1=int(input("Enter raised number: "))
        number2=int(input("Enter power number: "))
        result=number1**number2
        print("Result:",result)

    if isCorrect == 4:
        number1=int(input("Enter first number: "))
        number2=int(input("Enter second number: "))
        if choose==6:
                result=math.gcd(number1,number2)
                print("Result:",result)
        else:
                result=math.lcm(number1,number2)
                print("Result:",result)
    continues=str(input("Do you want to take another action? y/n: "))
    if continues=="y":
        continue
    elif continues=="n":
        break
    else:
        print("Wrong key pressed, application closes.")
        break