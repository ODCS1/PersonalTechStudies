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

            # VERIFICAR SE O LADO ESQUERDO ESTÁ ORDENADO
            if nums[l] <= nums[m]:
                # VERIFICAR SE O TARGET ESTÁ NO LADO ESQUERDO
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # VERIFICAR SE O LADO DIREITO ESTÁ ONDERNADO
            else:
                # VERIFICAR SE O TARGET ESTÁ DO LADO DIREITO
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return result



arr = [3,1]
target = 1
obj = Solution()
print(obj.search(arr, target))