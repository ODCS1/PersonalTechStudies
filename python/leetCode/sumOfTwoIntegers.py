# 371. Sum of Two Integers

from typing import List

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFFF

        while b != 0:
            sumWithoutCarry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            a, b = sumWithoutCarry, carry

        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)




a = -12
b = -8
obj = Solution()
print(obj.getSum(a, b))