# 167. Two Sum II - Input Array Is Sorted

from typing import List

# USANDO A LÓGICA ANTERIOR DO TWOSUM 1 -> O(n)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         map = {}

#         for i in range(len(numbers)):
#             dif = target - numbers[i]
#             if dif in map:
#                 return [map[dif] + 1, i+1]
            
#             map[numbers[i]] = i


# USANDO POINTERS
class Solution:
    def twoSum(self, numbers: List[int], target: int):
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l+1, r+1]
            
        return []


arr = [1,2,3,4,5,6,7,8]
target = 4
obj = Solution()
print(obj.twoSum(arr, target))