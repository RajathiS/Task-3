def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
mylist = [10, 501, 22, 37, 100, 999, 87, 351]
prime = [num for num in mylist if prime(num)]
print(prime)