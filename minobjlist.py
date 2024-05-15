import math
def calculate(n, m):
    if n < m:
        return 0
    ways = math.comb(m + n - 1, m - 1)
    return ways
if __name__ == '__main__':
    n = 9
    m = 5
    result = calculate(n, m)
    print(result)