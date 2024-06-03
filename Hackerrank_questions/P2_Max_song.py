playlist = [1,1,2,2,3,5]
print(playlist)

l1 = list(set(playlist))
print(l1)
l2=[]
for i in range(len(l1)-1):
    count = 0
    for j in range(len(playlist)-1):
        if l1[i] == playlist[j]:
            count = count + 1
        else:
            count = count
            l2.append(count)


print(l2)








# dict_playlist = {}
# for i in playlist:
#     l1.append(i)
#     count = 0
#     for j in playlist:
#         if i == j:
#             count = count+1
#             l2.append(count)

# print(l1)
# print(l2)