

# if logical_query:
#     opretions_if logical_query True


# if logical_query:
#     opretions_if logical_query True
# else:
#     opretions_if logical_query False


# if logical_query1:
#     opretions_if logical_query1 True
# elif logical_query2:
#     opretions_if logical_query2 True
# else:
#     opretions_if all logical_queryes False

# x = -1
# x = int(input('Set number: '))
# if x>0:
#     print('Positive')
# elif x<0:
#     print('Negative')
# else:
#     print('Zero')

# rez = 'Positive' if x > 0 else 'Negative'
# del x
# print(rez)

# x = 1; n = 10
# y = d = c = 0
# while x<=n:
#     print(x)
#     x += 1
# else:
#     print('End of loop!')
# while True:
#     if x % 2 != 0:
#         x += 1
#         continue
#     print(x)
#     x += 1
#     if x >= n:
#         break
# print()
# for item in object:
#     <operations>
# [else:
#     <else_operations>]
# x = 1; n = 10
# for item in range(x, n+1):
#     # print(item, end=' ')
#     pass
# print(item)

# for item in [1, 2, 5]:
#     print(item, end=' ')

# import sys


# while True:
#     x = int(input("Enter command: "))
#     if x == 0:
#         sys.exit()
#     print(x)

class MyEXP(ArithmeticError):
    x = 5
    print("Custom exception!", x)

try:
    y = 0
    if y ==0:
        raise MyEXP('y == 0')
    x = 5 / y
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except ArithmeticError as e:
    print('ArithmeticError:',e)
except Exception as e:
    print('Exception:',e)



