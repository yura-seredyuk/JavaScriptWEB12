
file = open("files/file.txt", 'r')
data = file.read()
print(data)
file.close()

# with open("files/file.txt", 'r') as file:
#     # data = file.read()
#     # data = file.readline()
#     data = file.readlines()
#     print(data)