def decimaltoBinary(n):
    assert int(n) == n, 'The number should be integer only'
    if n == 0:
        return 0
    return n % 2 + 10 * decimaltoBinary(int(n // 2))

print(decimaltoBinary(34))