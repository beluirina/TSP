def dfs_tsp(grafo, ciudad_actual, visitados, camino, distancia_total):

    # Si visitamos todo el grafo y si volvimos a A - devolver resultado
    if len(visitados) == len(grafo):
        if 'A' in grafo[ciudad_actual]:
            # SI A es parte del camino siguiente de donde estamos - Agregarla al camino y tambien su distancia a la distancia total.
            return camino + ['A'], distancia_total + grafo[ciudad_actual]['A']
        else:
            return None, float('inf')  # No esta conectado a la inicial, por ende DEAD END. Indicamos infinidad por no poder llegar al destino.

    mejor_camino = None #iniciamos vacio
    mejor_distancia = float('inf') # cualquier distancia calculada será menor que float('inf'), osea el primer valor calculado siempre va a poder reemplazar el valor inicial.

    # mirar vecinos
    for ciudad_vecina, distancia in grafo[ciudad_actual].items():
        if ciudad_vecina not in visitados:
            # si hay una cuidad que no visitamos - volver a ejecutar con nuevos datos ahora
            nuevo_camino, nueva_distancia = dfs_tsp(
                grafo,
                ciudad_vecina,
                visitados | {ciudad_vecina},  # agregamos la nueva ciudad a los visitados
                camino + [ciudad_vecina],     # agregamos al historiasl
                distancia_total + distancia   # tomamos nota de nueva distancia recorrida
            )

            # si la nueva distancia es mas chica que la ultima registrada - guardamos esa como nueva referencia
            if nueva_distancia < mejor_distancia:
                mejor_camino = nuevo_camino
                mejor_distancia = nueva_distancia

    return mejor_camino, mejor_distancia

# iniciemos la busqueda
def resolver(grafo, ciudad_inicial='A'):
    visitados = {ciudad_inicial}  #  ciudad inicial visitada
    camino_inicial = [ciudad_inicial]  # empezamos por cuidad inicial
    distancia_inicial = 0  # 0 recorrido efectuado.
    return dfs_tsp(grafo, ciudad_inicial, visitados, camino_inicial, distancia_inicial)


# resolvamos la comparativa de caminos tomados...
mejor_camino, mejor_distancia = resolver(grafo)

# y procedemos a mostrarlos...
print(f"Mejor camino encontrado: {mejor_camino}")
print(f"Distancia total: {mejor_distancia}")
