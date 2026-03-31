# LIST:
# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# 2. Given math scores, find how many scored centum: 100
# 3. Given scores, grade each score: A > 90, B > 80, C > 60, others D
# 4. Given scores, count students for each grade
# 5. Given numbers, reverse numbers [1, 2, 3] -> [3, 2, 1]
# 6. Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]
# 7. Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]
# 8. Sort given numbers 
# 9. Sum of given numbers
# 10. Find even, odd
# 11. Multiply by 2
# 12. Compare two lists for equality

# 1. Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

# bucket=0
# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i==100:
#         bucket=bucket+1
# print(bucket)

# 2. Given math scores, find how many scored centum: 100

# bucket=1
# x=[ "math 70","math 100","math 80", "math 100","math60","math100"]
# for i in x:
#     if i=="math 100":
#         bucket=bucket+1
# print(bucket)

# 3. Given scores, grade each score: A > 90, B > 80, C > 60, others D
# bucket=[]
# x=[56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]
# for i in x:
#     if i >=90:
#         bucket=bucket+["grade a "]
#     elif i >=80:
#         bucket=bucket+["grade b"]
#     elif i >=60:
#         bucket=bucket+["grade c"]
#     elif i >=50:
#         bucket=bucket+["grade d"]
# print(bucket)

# 4. Given scores, count students for each grade
# bucket=0
# students=["sanjay 399","arun 499","parithi 600"]
# **************THIS QUEATION DOUGHT ***************

# 5. Given numbers, reverse numbers [1, 2, 3] -> [3, 2, 1]
# x=[2,4,8,10]
# x.reverse()
# print(x)

# 6. Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]

# 7. Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]


# 8. Sort given numbers 
# x=[3,9,8,4]
# x.sort(reverse=True)
# print(x)

# 7 assending_order in this give number

# x=[3,9,8,4]
# x.sort()
# print(x)

# 8   given number decending_order

# x=[3,9,8,4]
# x.sort(reverse=True)
# print(x)

# 9. Sum of given numbers

# bucket=[]
# x=[1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     bucket=bucket+[i+1]
# print(bucket)


# 10. Find even, odd

# bucket=[]
# x=[1,2,3,4,5,6,7,8,9]
# for i in x:
#     if i %2==0:
#         bucket.append((i,"even"))
#     else:
#         bucket.append((i,"odd"))
# print(bucket)

# 11. Multiply by 2

# bucket=[]
# x=[1,2,3,4,5,6,7,8]
# for i in x:
#     bucket.append(i*2)
# print(bucket)    







