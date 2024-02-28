from typing import List

# MINHA PRIMEIRA SOLUÇÃO
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         soma: int = 0
#         pos: int = 0
#         volta: int = 1
#         resposta: List[int] = []
#         while (soma != target or len(resposta) < 2):
#             if (pos == len(nums)):
#                 pos = volta
#                 volta += 1
#                 soma = 0
#                 resposta = []
#             else:
#                 if (len(resposta) == 2):
#                     soma -= nums[pos - 1]
#                     resposta.pop()
#                     continue
#                 else:
#                     if (soma == 0):
#                         resposta.append(pos)
#                     else:
#                         resposta.append(pos)

#                     soma += nums[pos]

#                     pos += 1
        
#         return resposta


# SOLUÇÃO MELHOR
class Solution:
    def twoSum(self, nums: List[int], target: int) :
        map = {}

        for i, j in enumerate(nums):
            dif = target - j
            if (dif in map):
                return [map[dif], i]
            
            map[j] = i


lista: list = [0,-2, 0,-4,-5]
alvo: int = 0

obj:Solution = Solution()

print(obj.twoSum(lista, alvo))