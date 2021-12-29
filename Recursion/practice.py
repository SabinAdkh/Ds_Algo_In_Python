def fibb(n):
    if n in [0, 1]:
        return n
    else:
        return fibb(n-1)+fibb(n-2)


print(fibb(3))
