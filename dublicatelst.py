def intersection(arr1, arr2, arr3):
    common = [x for x in arr1 if x in arr2 and x in arr3]
    print(common)

lst_1 = [10, 53, 10, 55, 80, 50]
lst_2 = [60, 70, 55, 80, 100]
lst_3 = [30, 40, 15, 20, 30, 55, 70, 80]

intersection(lst_1, lst_2, lst_3)