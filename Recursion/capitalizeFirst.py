def capitalizeFirst(arr):
    new_arr = []
    if len(arr) == 0:
        return arr
    else:
        new_arr.append(arr[0].capitalize())
   
    return new_arr + capitalizeFirst(arr[1:])
print(capitalizeFirst(['str', 'bts']))