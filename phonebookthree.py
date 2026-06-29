storage=dict()

while True: 
    print("PHONE BOOK")
    print("option")
    print(" add\n delete \n print\n exit")
    option=(input("enter above your option:"))
    if option=="exit":
       print("exit thank you")
       break
    print(option)

    if option== "add" :
        name=(input("enter a contact name:"))
        number=(input("enter a contact number:"))
        storage.update({name:number})
        print(storage)

    elif option=="delete":
        name = input("enter a name: ")
    
    if name in storage:
        del storage[name]
   
    elif option=="print":  
        print("----PRINT----")
        for i in storage.items():
            print(i)


