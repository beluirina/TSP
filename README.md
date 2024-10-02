# Travelling Salesman Problem (TSP)
TSP is a classic algorithmic problem in the field of computer science and operations research, focusing on optimization. It seeks the shortest possible route that visits every point in a set of locations just once.

Inicial data:
````
# 10 citys to go through
grafo ={
 'A': {'F': 3, 'B': 1, 'I': 4,'D':1},
 'B': {'E': 9, 'C': 6, 'A': 1},
 'C': {'J': 3, 'B': 6},
 'D': {'A': 1, 'H': 5, 'J':2},
 'E': {'J': 9, 'B': 9,'F':10},
 'F': {'E': 10, 'J': 1, 'A': 3},
 'G': {'H': 3, 'I': 4},
 'H': {'G': 3, 'D': 5},
 'I': {'G':4,'A':4},
 'J': {'C': 3, 'D': 2, 'E':9, 'F': 1}
}

# Cities in a plane
coordenadas = {
'A': (0, 0),
'B': (1, 1),
'C': (7, 4),
'D': (0, 1),
'E': (2, 10),
'F': (0, 3),
'G': (5, 3),
'H': (3, 5),
'I': (3, 0),
'J': (6, 6)
}
````
![ver las ciudades en un mapa]([https://github.com/beluirina/TSP/blob/main/visual.png])

Code in folders! DFS, BFS and A* (heuristic search) applied.

