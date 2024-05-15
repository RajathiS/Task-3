def triplets(lst, key):
    return [(x, y, z) for x in lst for y in lst for z in lst if x + y + z == key]

list = [10, 20, 30, 9]
print(triplets(list, 59))