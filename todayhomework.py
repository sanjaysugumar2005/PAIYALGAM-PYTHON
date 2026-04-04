# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
# 3. Given scores, grade each score: A > 90, B > 80, C > 60, others D
# 4. Given scores, count students for each grade
# 5. Given numbers, reverse numbers input [1, 2, 3] -> output [3, 2, 1]
# 6. Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]
# 7. Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]
# 8. Sort given numbers 
# 9. Sum of given numbers
# 10 Find even, odd
# 11. Multiply by 2
# 12. Compare two lists for equality

# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i>=80:
#      print(i,"A grade")
#     elif i>=70:
#         print(i,"B grade")
#     elif i>=60:
#         print(i,"C grade")
#     elif i>=40:
#         print(i,"d grade")
#     else:
#         print("fail")
# *******************************************************
# bucket=0
# x=[1,2,3,4]
# for i in x:
#     bucket=bucket+i
#     print(bucket)
# **************************************
# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
# bucket=[]
# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i==100:
#         bucket += [i]
    
# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
# bucket=[]
# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i==100:
#         bucket=bucket+[i]
# print(bucket)
# # ******************************************************
# count=0
# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i==100:
#         count=count + 1
# print(count)
# ******************************************************



