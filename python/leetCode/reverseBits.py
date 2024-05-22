# 190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))

        return res


obj = Solution()
print(obj.reverseBits(2))