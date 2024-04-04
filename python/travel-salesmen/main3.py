from random import choice, randint
import math

n_cities = 17

# MATRIZ DE DISTÂNCIAS
distances = [[None for _ in range(n_cities)] for _ in range(n_cities)]


def get_position():
    positions = [None for _ in range(n_cities)]
    for i in range(n_cities):
        y = randint(0, 1001)
        x = randint(0, 1001)

        positions[i] = str(x) + "," + str(y)
    return positions


def get_distances():
    vetPosi = get_position()

    for l in range(n_cities):
        for c in range(n_cities):
            x1 = int(vetPosi[l].split(",")[0])
            y1 = int(vetPosi[l].split(",")[1])
            x2 = int(vetPosi[c].split(",")[0])
            y2 = int(vetPosi[c].split(",")[1])
            d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            distances[l][c] = d


# CALCULAR A DISTÂNCIA TOTAL PERCORRIDA POR UM CAMINHO
def get_total_distance(tour):

    total_distance = 0

    for i in range(n_cities - 1):
        total_distance += distances[tour[i]][tour[i+1]]

    total_distance += distances[tour[-1]][tour[0]]

    return total_distance

# EURÍSTICA DO VIZINHO MAIS PRÓXIMO
def random_nearest_neighbor_heuristic():
    get_distances()
    
    # AS CIDADES QUE AINDA NÃO FORAM VISITADAS
    unvisited = list(range(0, n_cities))
    tour = [choice(unvisited)]

    unvisited.remove(tour[0])

    while unvisited:
        
        next_city = min(unvisited, key= lambda city: distances[tour[-1]][city])
        tour.append(next_city)
        unvisited.remove(next_city)

    return tour

tour = random_nearest_neighbor_heuristic()

print(tour, "{:.2f}".format(get_total_distance(tour)))