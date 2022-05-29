import sys

with open("files/file.txt", 'a') as file:
    # file.write('Text text with\n')

    print('Data from print')
    print('Data from print', file=file)
    print('Data from print', file=sys.stdout)
