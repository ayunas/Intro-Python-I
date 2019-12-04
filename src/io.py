# file = open("sample.txt","a")

# file.write("I am adding to this file\n")
# file.write("More lines are being added to this file")

# file.close()


# file = open("sample.txt", "r+")

# for line in file:
#     print(line)

# texts = ['add this line\n', 'and this line\n', 'please add yet another line\n']

# file.writelines(texts)

# print(file.read())

# file.close()

with open('sample.txt') as file:
    for line in file:
        words = line.split()
        print words




















