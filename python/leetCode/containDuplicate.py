from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i, j in enumerate(nums):
            if j in map:
                return True
            else:
                map[j] = i
        return False


obj = Solution()

vet = [1, 3, 5, 7, 8, 9, 11, 1]

print(f"Contain Duplicate: {obj.containsDuplicate(vet)}")