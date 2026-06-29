# name="Sanjay Sugumar"
# name=name.upper()
# char_count=dict()
# for c in name:
#     count=char_count.get(c)
#     if count==None:
#         char_count.update({c:1})
#     else:
#         char_count.update({c:count+1})
# print(char_count)

# try:
#     x=int(input("num:"))
#     y=0
#     print(x/y)

# except ValueError:
#     print("Only Number Print")
# except ValueError:
#     print("zero not divisble")

# number=int(input("enter a number:"))
# if number > 0:
#     print(f"{number} -> Positive")
# elif number == 0:
#     print(f"{number} -> Zero")
# else:
#     print(f"{number} -> Negative")


fruits = ["apple", "banana", "cherry"]
print(" ".join(fruits))

classroom = ["sanjay", "parithi", "vihnu", "arun"]

print("parithi:", "present" if "parithi" in classroom else "absent",
      "| ram:", "absent" if "ram" not in classroom else "present")

classroom = ["sanjay", "parithi", "vihnu", "arun"]

# check parithi (using in)
if "parithi" in classroom:
    print("present")
else:
    print("absent")

# check ram (using not in)
if "ram" not in classroom:
    print("absent")
else:
    print("present")