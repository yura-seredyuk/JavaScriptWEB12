# int/float/bool
# list / array - список / масив
# tuple - кортеж
# dict - словник
# set / frozenset - множина
# str - рядок
# range - діапазон

# mutable: list, dict, set
# inmutable: tuple, frozenset, str, int, float, bool

l = [[1,2], 2]
l[0][0] = 5
print(l[0])
t = ([3,4],2)
t[0][0] = 6
print(t[0])