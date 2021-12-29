def capitalizeWords(arr):
    capital_arr = []
    
    if len(arr) == 0:
        return arr
    else:
        capital_arr.append(arr[0].upper())
    
    return capital_arr + capitalizeWords(arr[1:])

print(capitalizeWords(['i', 'love', 'nepal']))