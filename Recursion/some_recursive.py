def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
def somRecursive(arr, callback):
    if len(arr) == 1:
        return callback(arr[0])
    elif callback(arr[0]):
        return True
    else:
        return somRecursive(arr[1:], callback)
    
    
print(somRecursive([2, 6], isOdd))