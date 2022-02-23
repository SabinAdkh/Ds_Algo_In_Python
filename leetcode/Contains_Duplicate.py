nums = [1, 2, 3, 1]
unique = []

# for i in nums:
#     if i in unique:
#         print(True)
#     else:
#         unique.append(i)

# nums = tuple(nums)
# for num in nums:
#     if nums.count(num) > 1:
#         print(True)
    
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]==nums[j]:
            print(True)
       