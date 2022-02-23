# nums = [2, 7, 11, 15]
# target = 9
# ans = []
# for i in range(len(nums)): # loop from beggining to the last of the list
#     for j in range(i+1, len(nums)): # loop from second element to the last
#         if nums[i] + nums[j] == target:
#             ans.append(i)
#             ans.append(j)

# print(ans)




class Solution:
   def twoSum(self, nums, target):
       ans = []
       for i in range(len(nums)):
           for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                   ans.append(i)
                   ans.append(j)
       return ans 

s = Solution()
print(s.twoSum([2, 7, 9,3], 10))


nums = [2, 3, 7, 9, 4]
target = 11
ans = []
print([(i,j) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j]==target])
