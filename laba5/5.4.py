words = "ёжик пошел гулять возле ёлки"
count = 0
for word in words.split(" "):
    if word.strip()[0] == 'ё':
        count +=1
print(count)