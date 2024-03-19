# 238. Product of Array Except Self
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map = {}
        m = 1

        for i,j in enumerate(vet):
            m *= j
            map[i] = m

        m = 1
        for k in range(-1, (-1) * (len(vet)), -1):
            m *= int(vet[k])
            map[k] = m
        
        res = [None] * len(vet)
        print(map)
        for w in range(0, len(res)):
            if(w == 0):
                n = (-1)*(len(res)-(1))

                res[w] = map[n]
            elif(w == len(res) - 1):
                res[w] = map[len(vet) - 2]
            else:
                res[w] = map[w-1] * map[(-1)*(len(res) - (w+1))]
        return res

obj = Solution()
vet = [1,2,3,4]

print(f"Result: {obj.productExceptSelf(vet)}")