# count = 0
#f = open("all_tswift_lyrics.txt","r")
# for line in f:
#     words = line.split()
#     for x in words:
#         if x == "love":
#             count = count+1
# print("Love appears", count , "times.")
# f.close()

from collections import Counter
f = open("all_tswift_lyrics.txt","r")

for line in f:
    words = line.split()
    for x in words:
        #print(words)
        x = Counter(words)
        print(x)

f.close()
