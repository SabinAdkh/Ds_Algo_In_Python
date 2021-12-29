def fibb(n):
    if n in [0, 1]:
        return n
    else:
        return fibb(n-1)+fibb(n-2)


print(fibb(4))

# def fibb(n):
#     a = 0
#     b = 1
    
#     for i in range(n):
#         print(a)
#         sum = a + b
#         a = b
#         b = sum

# fibb(5)