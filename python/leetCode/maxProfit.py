from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maiorProfit = prices[0]
        menorProfit = prices[0]
        profit = maiorProfit - menorProfit

        for i,j in enumerate(prices):
            if menorProfit > j:
                menorProfit = j
                maiorProfit = j
            if maiorProfit < j:
                maiorProfit = j
            if profit < maiorProfit - menorProfit:
                profit = maiorProfit - menorProfit

        return profit
    

vet = [7,6,4,3,1]

obj: Solution = Solution()
print(obj.maxProfit(vet))