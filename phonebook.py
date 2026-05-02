# phonebook=(input("hello welcome to phone book"))
# phone=int(input("1.enter a name:","2.enter a phone number","3.enter a email"))   
#      name=(input("enter a name:"))
#      phone=int(input("enter a phone number:"))
#      email=(input("enter a email:"))

print("HELLO WELCOME TO PHONEBOOK")
phonebook=[]
while True:

    print(">(1).Name")
    print(">(2).Phone Number")
    # print(">(3).Email")
    # print(">(4).Exit")
    option=int(input("Select Number (1/2/3/4):"))

    if option==1:
        name=input("enter a name:")
        print("name saved",name)
    elif option==2:
        number=input("enter a phonenumber:")
        print("phonenumber saved",number)
    elif option==3:
        email=input("enter a email:")
        print("your email saved ",email)
    elif option==4:
        print("exit a phone book")
        break
    