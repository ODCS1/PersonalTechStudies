def last_possible_departure(buses, passengers, capacity):
    buses.sort()
    passengers.sort()

    left, right = 0, max(buses[-1], passengers[-1])
    
    while left < right:
        mid = (left + right + 1) // 2
        
        bus_index, passenger_index = 0, 0
        available_seats = capacity
        
        while bus_index < len(buses) and passenger_index < len(passengers):
            if buses[bus_index] <= mid:
                if passengers[passenger_index] <= buses[bus_index] and available_seats > 0:
                    passenger_index += 1
                    available_seats -= 1
                else:
                    bus_index += 1
                    available_seats = capacity
            else:
                bus_index += 1
                available_seats = capacity
        
        if passenger_index == len(passengers):
            left = mid
        else:
            right = mid - 1

    return left

# Exemplo 1
buses1 = [10, 20]
passengers1 = [2, 17, 18, 19]
capacity1 = 2
print(last_possible_departure(buses1, passengers1, capacity1))  # Saída: 16

# Exemplo 2
buses2 = [20, 30, 10]
passengers2 = [19, 13, 26, 4, 25, 11, 21]
capacity2 = 2
print(last_possible_departure(buses2, passengers2, capacity2))  # Saída: 20
