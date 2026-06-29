name = 'sanjay' 
list_name = list(name)
print(list_name)
letter = name[0] 
count = 1
i = 1
if list_name[i-1] != '*':
    while i < len(name):
        if letter == list_name[i]:
            list_name[i] = '*'
            count+=1
            print(count)
        i+=1
    print(letter, count) 
    print(list_name)