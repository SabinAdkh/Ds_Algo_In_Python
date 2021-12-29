def stringifyNumbers(obj):
    for key, item in obj.items():
        if type(item) is int:
            obj[key] = str(item)
        elif type(item) is dict:
            stringifyNumbers(item)
        # else:
        #     continue
    return obj

d = {'a':'1', 'b':2, 'c':3, 'd':4, 'e':{'f': [], 'g': 67}}

print(stringifyNumbers(d))

# for key, item in d.items():
#     print(item)





# for key, item in d.items():
#     if type(item) == int:
#         d[key] = str(item)
    
#     else:
#         continue
    
# print(d)