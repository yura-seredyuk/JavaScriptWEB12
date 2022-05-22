
# my_list = [1, 2, 3, 2, 5, 5, 2, 3]

# s = list(set(my_list))
# print(s)
# new_list = []

# for item in my_list:
#     if item in new_list:
#         continue
#     new_list.append(item)

# print(new_list)

# text = "this is sample is text"
# l = set(text.split(' '))
# print(l)
# s = set(my_list)

# ls = [8,2, 9,7]

# union = set.union(s, ls)
# union.add(99)

# union.update([88,77,66])
# print(union.difference([77,2,6,4]))
# union.discard(100)
# union.remove(77)


# print(union)
# print(len(union))

# fs = frozenset(union)
# fs.union([1,0])
# print(fs)

#  ------ string ---------
# text = '            soMe text       '.strip(' ')
# # .capitalize().lower().upper().title().center(20,'*')
# text = text.replace('o', 'l')
# print(text)
# print(text.find('T'))
# print(text.rfind('t'))
# # print(text.index('T'))
# l = list(text)
# l[0] = 'R'
# print(', '.join(l))

# def func(x, y=0, *args, **kwargs):
#     print(x,y,args,kwargs)
#     for index, item in enumerate(args):
#         print(index, item)


# func(4, 5, 1, 2, 3, 4, 5, key=4, r = 1000)


# def gen():
#     try:
#         yield 1
#         yield 2
#     except StopIteration as e:
#         print(e, 'Data is empty!')

# a = gen()
# print(next(a))
# print(next(a))
# print(next(a))


a = iter([1,2,3])

print(a)
print(next(a))
print(next(a))
print(next(a))


def foo(limit = 10):
    i = 0
    while True:
        yield i
        i += 1
        if i > limit:
            raise StopIteration()

a = foo(2)
print(a)
print(next(a))
print(next(a))
print(next(a))
# print(next(a))