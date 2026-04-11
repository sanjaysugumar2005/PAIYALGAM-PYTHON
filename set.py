# days={"mon","tue","wed","thu","fri","sat"}
# print(days)
# print(dir(set))



# days_week_end={"sat","sun","fri"}
# days_week_end.add("fri")
# days_week_end.add("fri")
# days_week_end.update(["mon","tue"])
# days_week_end.remove("mon")
# days_week_end.discard("mon")
# print(days_week_end)


n = int(input("Enter a number: ").strip())

if n % 2 == n:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

