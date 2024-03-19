# The Latest Time to Catch a Bus
from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        l = len(buses)
        busPosition = [[None for _ in range(capacity)] for _ in range(l)]
        p = 0
        # AJUSTAR
        for lin in range(l):
            for col in range(p, capacity):
                if passengers[col] < buses[col]:
                    busPosition[lin][col] = passengers[col]
                    p += 1
        print(busPosition)

        for lin in range(l-1, -1, -1):
            for col in range(capacity-1, -1, -1):
                if col > 0:
                    if (busPosition[lin][col] - busPosition[lin][col-1] > 1):
                        return busPosition[lin][col] - 1
                else:
                    if (busPosition[lin-1][len(buses[lin-1])-1] is None):
                        return busPosition[lin][0] - 1
                    
        
# 20 [17, 18, None]


b = [10,20]
p = [2,4,17,19]
c = 2
obj = Solution()
print(obj.latestTimeCatchTheBus(b,p,c))