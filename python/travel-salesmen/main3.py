from random import choice
import math

n_cities = 17

# MATRIZ DE DISTÂNCIAS
distances = [[None for _ in range(17)] for _ in range(17)]


dis = math.sqr()


def get_distances():
    pass


# CALCULAR A DISTÂNCIA TOTAL PERCORRIDA POR UM CAMINHO
def get_total_distance(tour):

    total_distance = 0

    for i in range(n_cities - 1):
        total_distance += distances[tour[i]][tour[i+1]]

    total_distance += distances[tour[-1]][tour[0]]

    return total_distance

# EURÍSTICA DO VIZINHO MAIS PRÓXIMO
def random_nearest_neighbor_heuristic():
    
    # AS CIDADES QUE AINDA NÃO FORAM VISITADAS
    unvisited = list(range(0, n_cities))
    tour = [choice(unvisited)]
    # print(id(tour))
    unvisited.remove(tour[0])

    while unvisited:
        
        next_city = min(unvisited, key= lambda city: distances[tour[-1]][city])
        tour.append(next_city)
        unvisited.remove(next_city)

    return tour
# print(type(random_nearest_neighbor_heuristic()))
tour = random_nearest_neighbor_heuristic()
# print(tour)
print(tour, get_total_distance(tour))