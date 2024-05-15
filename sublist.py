def sublist(arr):
    sum_map = {}
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0 or curr_sum in sum_map:
            return True
        sum_map[curr_sum] = i
    return False
array = [4, 2, -3, 1, 6]
print(sublist(array))
