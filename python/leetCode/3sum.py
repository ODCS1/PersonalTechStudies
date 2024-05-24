# 15. 3Sum

from typing import List

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         map = {}
#         l, r = 0, len(nums) - 1

#         while l < r:
#             curSum = nums[l] + nums[r]

#             if -curSum in map:
#                 return [-curSum, l, r]
            
#             map[nums[l]] = l
#             map[nums[r]] = r

#             l += 1
#             r -= 1


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            curSum = 0

            while l < r:
                curSum = nums[l] + nums[r] + a

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1

        return result

arr = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(arr))
