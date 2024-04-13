from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        currentProduct = 1

        for i in range(len(nums)):
            if currentProduct < 0:
                currentProduct = 0

            currentProduct *= nums[i]
            maxProduct = max(maxProduct, currentProduct)
        
        return maxProduct
    

# vet = [-3,-1,-1]
vet = [-2,0,-1]
obj = Solution()
print(obj.maxProduct(vet))