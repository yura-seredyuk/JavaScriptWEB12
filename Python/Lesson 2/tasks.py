# """Description for module:
# ...
# """
# from email.quoprimime import body_check
# import sys


# try:
#     task = int(input("Chouse task number:\n\
#     \t1. Oil calculator\n\
#     \t2. Mobile calculator\n\
#     \t0. Exit\n>> "))
#     if task == 1:
#         """
#         1.Дано витрати машиною пального на 100 км, 
#             ціну 1 л пального, а також шлях, який потрібно проїхати водію. 
#             Обчислити та вивести на екран скільки потрібно витратити грошей 
#             водію, щоб проїхати вказаний шлях.
#         """

#         # costs = 9
#         # cost = 40
#         # distance = 10

#         # pay = costs / 100 * distance * cost
#         # print(pay)


#         # costs = int(input('Enter costs per 100km: '))
#         # cost = int(input('Enter cost per 1L: '))
#         # distance = int(input('Enter distance in km: '))

#         # pay = costs / 100 * distance * cost
#         # print(f"You muat to pay {pay}UAH!")

#         try:
#             costs = int(input('Enter costs per 100km: '))
#             cost = int(input('Enter cost per 1L: '))
#             distance = int(input('Enter distance in km: '))
#             if costs<=0 or cost<=0 or distance <=0:
#                 raise ValueError
#             pay = costs / 100 * distance * cost
#             print(f"You must to pay {pay}UAH!")
#         except ValueError:
#             print("\nError! Uncorrect values!")

#     elif task == 2:
#         """2. Користувач вказує ціну однієї хвилини вихідного дзвінка з одного
#             мобільного оператора іншому, а також тривалість розмови. 
#             Необхідно обрахувати грошову сумму, на яку був здійснений дзвінок
#         """

#         try:
#             cost = int(input('Enter cost per 1m: '))
#             time = int(input('Enter time in m: '))
#             if cost<=0 or time <=0:
#                 raise ValueError
#             pay = time * cost
#             print(f"You must to pay {pay}UAH!")
#         except ValueError:
#             print("\nError! Uncorrect values!")

#     elif task == 0:
#         sys.exit()
# except Exception as e:
#     print("Error! ",e)
# finally:
#     print('Programm comleted!')

#    ------------ functions ------------
# # def name(attributes):
# #     body
# #     [return]

"""Description for module:
...
"""
import sys


def oil_calculator():
    """1.Дано витрати машиною пального на 100 км, 
        ціну 1 л пального, а також шлях, який потрібно проїхати водію. 
        Обчислити та вивести на екран скільки потрібно витратити грошей 
        водію, щоб проїхати вказаний шлях.
    """
    try:
        costs = int(input('Enter costs per 100km: '))
        cost = int(input('Enter cost per 1L: '))
        distance = int(input('Enter distance in km: '))
        if costs<=0 or cost<=0 or distance <=0:
            raise ValueError
        pay = costs / 100 * distance * cost
        print(f"You must to pay {pay}UAH!")
    except ValueError:
        print("\nError! Uncorrect values!")

def mobile_calculator():
    """2. Користувач вказує ціну однієї хвилини вихідного дзвінка з одного
        мобільного оператора іншому, а також тривалість розмови. 
        Необхідно обрахувати грошову сумму, на яку був здійснений дзвінок.
    """
    try:
        cost = int(input('Enter cost per 1m: '))
        time = int(input('Enter time in m: '))
        if cost<=0 or time <=0:
            raise ValueError
        pay = time * cost
        print(f"You must to pay {pay}UAH!")
    except ValueError:
        print("\nError! Uncorrect values!")

try:
    task = int(input("Chouse task number:\n\
    \t1. Oil calculator\n\
    \t2. Mobile calculator\n\
    \t0. Exit\n>> "))
    if task == 1:
        oil_calculator()
    elif task == 2:
        mobile_calculator()
    elif task == 0:
        sys.exit()
except Exception as e:
    print("Error! ",e)
finally:
    print('Programm closed!')
