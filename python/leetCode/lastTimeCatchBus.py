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




















# from typing import List

# class Solution:
#     def latest_time_catch_the_bus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
#         # Sort the buses and passengers in ascending order to process them in sequence
#         buses.sort()
#         passengers.sort()
      
#         passenger_index = 0  # index of the current passenger in the sorted list
#         # Iterate through buses to see how many passengers each can pick up
#         for bus_arrival_time in buses:
#             current_capacity = capacity  # Track the current bus's remaining capacity
#             # Board passengers until the bus is full or no more passengers for the bus
#             while current_capacity > 0 and passenger_index < len(passengers) and passengers[passenger_index] <= bus_arrival_time:
#                 # Load a passenger and decrease the available capacity
#                 current_capacity -= 1
#                 passenger_index += 1
      
#         # Adjust the index back to the last boarded passenger
#         passenger_index -= 1
      
#         # Latest possible time to catch the bus is either bus's last arrival time
#         # or just a minute before the last passenger boarded if the bus is full
#         latest_time = buses[-1] if current_capacity > 0 else passengers[passenger_index]
      
#         # If the bus is full, find the latest time by subtracting from the last boarded passenger's time,
#         # making sure there's no passenger at that time already
#         while passenger_index >= 0 and passengers[passenger_index] == latest_time:
#             latest_time -= 1
#             passenger_index -= 1
      
#         # Return the latest time a passenger can catch the bus
#         return latest_time


# b = [10,20]
# p = [2,4,11,20]
# capacity = 2
# obj = Solution()
# print(obj.latest_time_catch_the_bus(b,p,capacity))
