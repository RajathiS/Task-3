def happy(num):
    while num != 1 and num != 4:
        temp_sum = 0
        for digit in str(num):
            temp_sum += int(digit) ** 2
        num = temp_sum
    return num == 1
def happy_numbers(nums):
    happy_nums = []
    for num in nums:
        if happy(num):
            happy_nums.append(num)
    return happy_nums

a = [200, 501, 10, 37, 1000, 999, 87, 100, 13]
print(happy_numbers(a))
