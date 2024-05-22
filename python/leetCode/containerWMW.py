# 11. Container With Most Water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1

        while l < r:
            currHeight = min(height[l], height[r])
            currArea = (r - l) * (currHeight)

            result = max(result, currArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        
        return result

arr = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(arr))