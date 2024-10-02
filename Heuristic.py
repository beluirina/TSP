import heapq

def heuristic(a, b, coordenadas):
    # Usamos la distancia de Manhattan como heurística
    return abs(coordenadas[a][0] - coordenadas[b][0]) + abs(coordenadas[a][1] - coordenadas[b][1])

def a_star_tsp(grafo, start, coordenadas):
    # Inicializamos la cola de prioridad
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start], 0))  # (costo acumulado, nodo actual, camino recorrido, número de nodos visitados)

    best_path = None
    best_cost = float('inf')

    # Mientras haya elementos en la cola de prioridad
    while priority_queue:
        current_priority, current, path, nodes_visited = heapq.heappop(priority_queue)

        # Si hemos visitado todos los nodos y estamos de vuelta en el nodo inicial
        if nodes_visited == len(grafo) and current == start:
            if current_priority < best_cost:
                best_cost = current_priority
                best_path = path
            continue

        # Iteramos sobre los vecinos
        for neighbor, weight in grafo[current].items():
            if neighbor not in path:  # Evitamos volver a visitar el mismo nodo
                new_cost = current_priority + weight
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path, nodes_visited + 1))

        # Si hemos visitado todos los nodos pero aún no estamos en el nodo inicial, volvemos a 'start'
        if nodes_visited == len(grafo) - 1 and current != start:
            heapq.heappush(priority_queue, (current_priority + heuristic(current, start, coordenadas), start, path + [start], nodes_visited + 1))

    return best_path, best_cost

start_node = 'A'
path, cost = a_star_tsp(grafo, start_node, coordenadas)

if path:
    print(f"Ruta que visita todas las ciudades y regresa a {start_node}: {path} y el costo total fue de {cost}")
else:
    print("No se encontró una ruta que visite todas las ciudades.")
