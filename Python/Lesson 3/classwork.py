# int/float/bool
# list / array - список / масив  [1, 2, 3, 3]
# tuple - кортеж (1, 2, 3, 3)
# dict - словник {'key1':1, 'key2':2}
# set / frozenset - множина {1,2,3,4}
# str - рядок 'text'
# range - діапазон [0,1,2,3,4]

# mutable: list, dict, set
# inmutable: tuple, frozenset, str, int, float, bool

# l = [[1,2], 2]
# l[0][0] = 5
# print(l[0])
# t = ([3,4],2)
# t[0][0] = 6
# print(t[0])


# x = 5
# print(id(x))
# del x
# x = 5
# print(id(x))

# --------- list -------------
# y = int(4.5)
# x = [1,2,3]
# x = list((1,2,3))
# x = list('text')
# print(x)


# l = [1,5,2,6,3]
# l2 = l
l = [1,5,2,5,6,3]
# print(l)
# l2 = l[:]
# l2 = l.copy()
# l2 = list(l)
# import copy
# l2 = copy.deepcopy(l)

# l[0] = 5
# l2[1] = 0
# print(id(l))
# print(id(l2))
# print(l)
# print(l2)
# print(l[-2])
# print(len(l))
# print(len('text'))
# print(str(l))
# print(min(l))
# print(max(l))

# ---- list methods ---------
# l.append(100)
# l.append([1,2])
# c = [3,5]
# l.append(c)
# l.extend('tetx')
# l.extend(c)
# l.insert(1,9999)
# a = l.pop(-1)
# del l[-1]
# l.remove(100)
# print(l)
# print(a)
# print(l.index(5,3,5))
# print(99 in l)
# print(l.count(5))
# print(sorted(l, reverse=True))
# l.sort(reverse=True)
# # l.clear()
# l = []
# print(l)

# a = []
# for i in range(1,11):
#     a.append(i)
# print(a) 

# ----- list comprehantion --------
# b = [ i for i in range(1,11)]
# b = [ i for i in range(1,11) if i % 2 == 0]
# b = [ i for i in range(1,11,2)]
# print(b)

# c = []
# for i in range(1, 4):
#     for j in range(1,4):
#         c.append([i,j])

# # c[0].append([5])

# print(c)
# print(c[0])
# print(c[0][0])

# d = [[i,j] for i in range(1,4) for j in range(1,4)]
# print(d)

# f = []
# for i in d:
#     for j in i:
#         f.append(j)

# print(f)

# h = [j for i in d for j in i]
# print(h)

# e = [0] * 10

# print(e)

# r = [[0 for i in range(1,4)] for j in range(1,4)]
# print(r)

