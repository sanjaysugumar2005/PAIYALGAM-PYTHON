def can_vote():
    min_age = 18
    age = int(input("Enter your age: "))

    if age >= min_age:
        print("Can vote")
    else:
        print("Cannot vote")

can_vote()