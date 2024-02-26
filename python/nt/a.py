class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        soma: int = 0
        pos: int = 0
        volta: int = 1
        resposta: list[int] = []
        while (soma != target):
            if (pos == len(nums)):
                pos = volta
                volta += 1
                soma = 0
                resposta = []
            else:
                if (len(resposta) == 2):
                    soma -= nums[pos - 1]
                    resposta.pop()
                    continue
                else:
                    if (soma == 0):
                        resposta.append(pos)
                    else:
                        resposta.append(pos)

                    soma += nums[pos]

                    pos += 1
        
        return resposta
    

lista: list = [3, 3]
alvo: int = 6

obj:Solution = Solution()

print(obj.twoSum(lista, alvo))