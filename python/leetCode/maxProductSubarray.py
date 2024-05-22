from typing import List

# Dynamic Programming

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        maxCurrrentProduct, minCurrentProduct = 1, 1

        for n in nums:
            if n == 0:
                minCurrentProduct, maxCurrrentProduct = 1, 1
                continue
            
            aux = maxCurrrentProduct * n
            maxCurrrentProduct = max(n * maxCurrrentProduct, n * minCurrentProduct, n)  
            minCurrentProduct = min(aux, n * minCurrentProduct, n)  

            result = max(result, maxCurrrentProduct)


        return result
    

vet = [-4,-3,-2]
obj = Solution()
print(obj.maxProduct(vet))