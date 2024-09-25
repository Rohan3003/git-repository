playlist = [1,1,2,2,3,5]
print(playlist)
for i in range(len(playlist)):
    if playlist[i] == playlist[i+1]:
        fav_singer.append(playlist[i])