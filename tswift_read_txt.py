count = 0
f = open("all_tswift_lyrics.txt","r")
for line in f:
    love_count = line.find("love")
    for x in love_count:
        if x == "love":
            count = 0+1
            print(count)
f.close()
