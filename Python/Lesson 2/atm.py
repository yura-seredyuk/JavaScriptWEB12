# data base:
money = 100000
password = 1111

count = 0
while True:
    passwd = int(input("Enter password: "))
    if passwd == password:
        break
    print('Incorrect password!')
    count += 1
    if count == 3:
        print('Your card is blocked!')
        break

print('Chouse command:')