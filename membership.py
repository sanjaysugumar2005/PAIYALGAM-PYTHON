
# #single line class
# classroom = ["sanjay", "parithi", "vihnu", "arun"]

# print("parithi:", "present" if "parithi" in classroom else "absent",
#       "| ram:", "absent" if "ram" not in classroom else "present")

# classroom = ["sanjay", "parithi", "vihnu", "arun"]

# # check parithi (using in)
# if "parithi" in classroom:
#     print("present")
# else:
#     print("absent")

# # check ram (using not in)
# if "ram" not in classroom:
#     print("absent")
# else:
#     print("present")

# print("Python".find("java"))  
# print("Python".find("th")) 

def greet():
    print("Hello World!")
    
def hello(name):
    print("Hello", name)        

def add(x, y):
    return x + y

def increment(x, y = 1):
    return x + y

greet()                         # Hello World!
hello("John")                    # Hello John!

total = add(10, 20)
print(total)                    # 30

result = increment(10)
print(result)                   # 11 

