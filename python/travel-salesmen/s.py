cities = [200, 300, 100, 500, 400]

#population_diference = [[None for _ in range(cities)] for _ in range(cities)]
population_diference = [
    [  0,-100, -200, -300, -400],
    [100,   0, -100, -200, -300],
    [200, 100,    0, -100, -200],
    [300, 200,  100,    0, -100],
    [400, 300,  200,  100,    0]
]

def getTotalPopulation():
    total = 0
    for i in range(len(cities)):
        total += cities[i]
    return total

def getMostPopulationCity(m):
    unvisitedCities = list(range(len(cities))) # Lista com todas as cidades disponiveis
    if m < len(cities):
        tour = [[] for _ in range(m)]              # Lista que armazenara as cidades vizitadas pelos caixeiros

        while unvisitedCities:                     # No While visitamos as cidades nao visitadas pelo seu tamanho de populacao,
            nextCity = max(unvisitedCities, key = lambda city: cities[city])  # pegamos a maior cidade e a removemos da lista das cidades
            unvisitedCities.remove(nextCity)                                  # disponiveis ja que ela ja foi visitada.
            tour[len(unvisitedCities) % m].append(nextCity)               

        arr = []
        for p in range(len(tour)):
            travelingSalesman = [cities[city] for city in tour[p]]
            arr.append(travelingSalesman)          # Formata o arranjo para aparecer a quantidade de populacao.

        for l in 
        for lin in range(len(arr)):
            for col in range(len(arr[lin])):
                arr_population_diff[lin][col] = 
        
        for i in range(len(arr)):
            print(arr)
        print(arr[1][1])
        return arr
    else:
        return "Error"

def getPopulationDiference():
    for i in range(len(cities)):
        for j in range(len(cities)):
            population_diference[i][j] = cities[j] - cities[i]

print(getMostPopulationCity(2))
print(getTotalPopulation())

if __name__ == "main":

    arr = getMostPopulationCity()