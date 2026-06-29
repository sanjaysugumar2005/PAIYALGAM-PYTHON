# Print numbers from 1 to 10 using a while loop
# x=1
# while x<=10:
#     print(x)
#     x=x+1

# Print numbers from 10 to 1 (reverse)
# x=1
# while x>=10:
#     print(x)
#     x=x-1
# Print even numbers from 1 to 20
# Print odd numbers from 1 to 20
# numbers = [10, 30, 20, 40]
# numbers.extend(60, 70)
# print(numbers)
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print(numbers[0])        # 10
# numbers[-1]       # 80
# numbers[2:5:1]    # [30, 40, 50]
# numbers[:4]       # [10, 20, 30, 40]
# numbers[3:]       # [40, 50, 60, 70, 80]
# numbers[::-1]     # [80, 70, 60, 50, 40, 30, 20, 10]  reverse
# print(numbers)
# name="sanjay"
# print(name[4:])
# numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# print(numbers[-1])


# data="sanjay,50,60,70,80,90"
# data=data.split(",")
# data=data[1:len(data):1]
# data=int(data)
# print(data)


# x = "50"
# x = int(x)
# print(x)
# print(type(x))

# print(data)
# for i in data:
#     if i in (1,2,3,4,5,6,7,8,9,0):
#         print(i)



# data="sanjay,50,60,70,80,90"
# data=data.split(",")
# data=data[1:]
# total=0
# for x in data:
#      x=int(x)
#      total=total+x
# print(total)

# for i in range(5):
#     print(i)
#     i = 1
# x=1
# while x <= 6:
#     print(x)
#     x=x+1
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))