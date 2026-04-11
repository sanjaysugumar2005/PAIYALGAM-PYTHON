# CALCULATOR:

exit=False

while exit!=True:
    option=input("enter a option,add,sub,mul,divi,exit:")

    if option=="exit":
        exit=True   
        continue

    num1=int(input("enter a number one:"))
    num2=int(input("enter a number two:"))

    if option=="add":
        print(num1+num2)
    elif option=="sub":
        print(num1-num2)
    elif option=="mul":
        print(num1*num2)
    elif option=="divi":
        print(num1/num2)
    else:
        print("in vaild")
        
print("calcultor stop")