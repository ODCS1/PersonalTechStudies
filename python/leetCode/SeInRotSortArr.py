# 33. Search in Rotated Sorted Array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                result = m
                break

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return result



arr = [4,5,6,7,0,1,2]
target = 4 # DÁ CERTO
# target = 0 DÁ ERRADO
obj = Solution()
print(obj.search(arr, target))