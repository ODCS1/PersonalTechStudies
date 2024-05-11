# 167. Two Sum II - Input Array Is Sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(numbers)):
            dif = target - numbers[i]
            if dif in map:
                return [map[dif] + 1, i+1]
            
            map[numbers[i]] = i


arr = [1,2,3,4,5,6,7,8]
target = 4
obj = Solution()
print(obj.twoSum(arr, target))