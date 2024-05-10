# 167. Two Sum II - Input Array Is Sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        l, r = 0, len(numbers) - 1

        while l <= r:
            m = (l + r) // 2

            if target <= numbers[m]:
                r = m - 1
            else:
                
                pass


arr = [1,2,3,4,5,6,7,8]
target = 4
obj = Solution()
print(obj.twoSum(arr, target))