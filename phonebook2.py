# contact=[]
# while True:
#     print("CONTACT MENU")
#     print("1.name and number")
#     print("2.search contact")
#     print("3.delete")
#     print("4.exit")
#     choice=input("you choice number (1,2,3,4):")
#     if choice=="1":
#         name=input("enter a name:")
#         number=int(input("enter a number:"))
#         contact=contact+[[name,number]]
#     elif choice=="2":
#         name=input("enter a name to search:")
#         found=False
#         for c in contact:
#            if c[0]== name:
#             print("Found :",c[0],"-",c[1])
#             found=True
#             break
#         if not found:
#             print("not found")