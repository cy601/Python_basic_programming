file = open("Walden.txt", "r")
words = []
for line in file:
    for word in line.replace('\n', '').split(" "):
        words.append(word)

map = {}
for word in words:
    map[word] = map[word] + 1 if word in map.keys() else 1

for key in map:
    print(key + ": " + str(map[key]))
