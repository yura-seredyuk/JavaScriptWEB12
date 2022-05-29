# w - create and write / rewrite
# a - append - open and fite from EOF 
# r - read
# x - create file if it not exixsts


# file = open("files/file.txt", 'a')
# file.write('Text text\n')
# file.close()

with open("files/file.txt", 'a') as file:
    file.write('Text text with\n')

print(file)