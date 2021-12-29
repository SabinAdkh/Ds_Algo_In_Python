def productOfArray(arr):
    start = 0
    if len(arr) == 0:
        return 1
    return arr[start] * productOfArray(arr[start+1:])


print(productOfArray([2, 3, 5, 6, 7]))