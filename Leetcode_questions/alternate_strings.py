word1 = "abc"
word2 = "pqrst"

list1 = [char for char in word1]
list2 = [char for char in word2]

# print(list1)
# print(list2)
list3 = []

if len(list1) > len(list2):
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
else:
    for i in range(len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])

print(list3)
        