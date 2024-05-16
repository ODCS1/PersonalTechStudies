# 191. Number of 1 Bits

from typing import List

class Solution:
    # FIRST SOLUTION
    def hammingWeight1(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result

    # SECOND SOLUTION
    def hammingWeight2(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result



obj = Solution()
print(obj.hammingWeight1(3))
print(obj.hammingWeight2(3))