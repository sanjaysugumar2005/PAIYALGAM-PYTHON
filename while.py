# x=1
# while x<=5:
#     print(x*2)
#     x=x+1

# print("---")    

# x=2

# while x<=10:
#     print(x*1)
#     x=x+2

# def mul():
#     x=1
#     while x<=10:
#         z=x+0
#         x=x*2
#         print(z,"x 2 =",x)
        
# mul()

# def tab(num):
#     x=1
#     while x<=10:
#         print(x, "x", num  ,"=", x * num)
#         x=x+1


# tab(5)
# tab(3)
##############################8 QUETION WORK ###########################################
 # 1. Print 1, 2, 3 … 10
# x=1
# while x<=10:
#     print(x*1)
#     x=x+1

# # 2. Print 2, 4 ,6 … 20

# x=1
# while x<=20:
#     print(x*1)
#     x=x+1

# 3. Print  Table given a number 
#  a. Ex: 2 -> 1x2, 2x2, 3x2 … 10x2

# def (num):
#     x=1
#     while x<=10:
#         print(x,"x",num,"=",x*num)
#         x=x+1
# table(4)
# table(6)

# 4. Fi)nd all odd numbers until given number
#  a. Ex: 10 -> 1, 3, 5, 7, 9

# def odd(num):
#     x=1
#     while x<=num:
#         if x%2!=0:
#             print(x)
#         x+=1
# odd(19)


# 5. Find all numbers divisible by 3 until given number
# def divi():
#     x=1
#     while x<=10:
#         if x%3==0:
#             print(x)
#         x=x+1       
# divi()


# 6. Find all numbers divisible by 3 and 5 until given number
#  a. Ex: 50 -> 15, 30, 45

# def divi(num):
x=1
while x <=50:
    if x%3==0 and x%5==0:
            print(x)
    x=x+1
# divi(50)

# 7. Sum of natural numbers until given number
#  a. Ex: input:  4  ->  1 + 2 + 3 + 4 ->  10

# def nat(num):
#     total=0
#     x=1
#     while x<=num:
#         total=x+total
#         x=x+1
#         print(total)
# nat(4)


# 8. Find factorial of given number
#  Ex: input 5 ->  5 * 4 * 3 * 2 * 1 -> 120

# def fat():
total=1
x=1
while x<=6:
    total=x*total
    x=x+1

print(total)
# fat()

# text = "Python"
# print(text[0:3])
student = {
    "name":"Sanjay",
    "mark":90
}

print(student.keys())
print(student.values())
print(student.items())

text = "hello world"

print(text.upper())
print(text.lower())
print(text.split())
print(text.replace("world","python"))
