from collections import deque

def bfs(grafo, ciudad_inicial='A'):
    # almacenar datos en formato (camino, distancia_total)
    cola = deque([([ciudad_inicial], 0)])  # Empezamos
    mejor_camino = None
    mejor_distancia = float('inf')  # Mismo concepto anterior. Valor alto de inicio para comparativa.

    while cola:
        camino, distancia_total = cola.popleft()  # extraemos el primer elemento
        ciudad_actual = camino[-1]  # ultima ciudad visitada en el camino

        # Si visitamos todas las ciudades y estamos de vuelta en la ciudad inicial
        if len(camino) == len(grafo) + 1 and camino[-1] == ciudad_inicial:
            if distancia_total < mejor_distancia:  # mejor distancia? guardame estos datos entonces
                mejor_camino = camino
                mejor_distancia = distancia_total
            continue

        # camino del momento..
        for ciudad_vecina, distancia in grafo[ciudad_actual].items():
            # si no la habiamos visitado OR en nuestro camino esta A? ya recorrimos todo?
            if ciudad_vecina not in camino or (ciudad_vecina == ciudad_inicial and len(camino) == len(grafo)):
                nuevo_camino = camino + [ciudad_vecina]
                nueva_distancia = distancia_total + distancia
                cola.append((nuevo_camino, nueva_distancia))  # registramos camino y distancia

    return mejor_camino, mejor_distancia


# llamemos y registremos resultados
mejor_camino, mejor_distancia = bfs(grafo)

# mostramos.
print(f"Mejor camino encontrado: {mejor_camino}")
print(f"Distancia total: {mejor_distancia}")
