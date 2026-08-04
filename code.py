# # # # def reverse_string(s):
# # # #     return s[::-1]

# # # # text = input("Enter a string: ")
# # # # print("Reversed:", reverse_string(text))

# # # def add(no1, no2 ):
# # #     return no1+no2
# # # def subration(no1,no2):
# # #     return no1-no2
# # # def divide(no1,no2):
# # #     return no1//no2
# # # developer="nirmal anad"
# # # import function_demo
# # # result=function_demo.add(100,150)
# # # print(result)

# # # # def add(no1, no2):
# # # #     return no1 + no2

# # # # def subtraction(no1, no2):
# # # #     return no1 - no2

# # # # def divide(no1, no2):
# # # #     return no1 // no2

# # # # developer = "Nirmal Anand"

# # # num = 10

# # # result = "Even" if num % 2 == 0 else "Odd"

# # # print(result)

# # # marks = 45

# # # result = "Pass" if marks >= 35 else "Fail"

# # # print(result)

# # # a = 10
# # # b = 30
# # # c = 20

# # # largest = a if a > b and a > c else b if b > c else c

# # # print("Largest:", largest)

# # Even
# # 2. Check Positive or Negative
# # num = -5

# # result = "Positive" if num >= 0 else "Negative"

# # print(result)

# # Output

# # Negative
# # 3. Voting Eligibility
# # age = 20

# # result = "Eligible to Vote" if age >= 18 else "Not Eligible"

# # print(result)

# # Output

# # Eligible to Vote
# # 4. Largest of Two Numbers
# # a = 15
# # b = 25

# # largest = a if a > b else b

# # print("Largest:", largest)

# # Output

# # Largest: 25
# # 5. Pass or Fail
# # marks = 45

# # result = "Pass" if marks >= 35 else "Fail"

# # print(result)

# # Output

# # Pass
# # 6. Check Adult or Minor
# # age = 16

# # status = "Adult" if age >= 18 else "Minor"

# # print(status)

# # Output

# # Minor
# # 7. Maximum of Three Numbers (Nested Ternary)
# # a = 10
# # b = 30
# # c = 20

# # largest = a if a > b and a > c else b if b > c else c

# # print("Largest:", largest)

# # Output

# # Largest: 30
# # 8. Function Using Ternary Operator
# # def check_number(num):
# #     return "Positive" if num > 0 else "Negative"

# # print(check_number(12))
# # print(check_number(-7))

# # Output

# # Positive


# def beginning_zeros(a: str) -> int:
#     # your code here
#     return 0


# print("Example:")
# print(beginning_zeros("10"))

# # These "asserts" are used for self-checking
# assert beginning_zeros("100") == 0
# assert beginning_zeros("001") == 2
# assert beginning_zeros("100100") == 0
# assert beginning_zeros("001001") == 2
# assert beginning_zeros("012345679") == 1
# assert beginning_zeros("0000") == 4

# print("The mission is done! Click 'Check Solution' to earn rewards!")


text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


    num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


    n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


    a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print("Largest:", largest)