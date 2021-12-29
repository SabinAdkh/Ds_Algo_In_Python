def flatten(arr):
    new_arr = []
    for item in arr:
        if type(item) is list:
            new_arr.extend(flatten(item))
        else:
            new_arr.append(item)
    return new_arr
print(flatten([4, 7,[5, 6]]))