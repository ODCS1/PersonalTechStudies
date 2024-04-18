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

            maxCurrrentProduct = max(maxCurrrentProduct * n, minCurrentProduct * n, n)  
            minCurrentProduct = min(maxCurrrentProduct * n, minCurrentProduct * n, n)  

            result = max(maxCurrrentProduct, result)


        return result

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         result = max(nums)
#         minCurrentProduct, maxCurrentProduct = 1, 1

#         for n in nums:
#             if n == 0:
#                 minCurrentProduct, maxCurrentProduct = 1, 1
#                 continue
            
#             maxCurrentProduct = max(maxCurrentProduct * n, minCurrentProduct * n, n)
#             minCurrentProduct = min(maxCurrentProduct * n, minCurrentProduct * n, n)

#             result = max(maxCurrentProduct, result)

#         return result
    

# vet = [-3,-1,-1]
vet = [-4,-3,-2]
# vet = [-2,0,-1, 2]
obj = Solution()
print(obj.maxProduct(vet))