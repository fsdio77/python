s = input("введите строку\n")
c =0
for word in s.split(" "):
    if word.strip()[0] == 'р':
        c += 1
print(c)