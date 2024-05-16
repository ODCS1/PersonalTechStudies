# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            m = i
            currResult = 0
            while m:
                m &= (m - 1)
                currResult += 1
            ans.append(currResult)
        
        return ans
    
val = 5
obj = Solution()
print(obj.countBits(5))