# 15. 3Sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        map = {}
        l, r = 0, len(nums) - 1

        while l < r:
            curSum = nums[l] + nums[r]

            if -curSum in map:
                return [-curSum, l, r]
            
            map[nums[l]] = l
            map[nums[r]] = r

            l += 1
            r -= 1

arr = [3,4,0,-3]
obj = Solution()
print(obj.threeSum(arr))
