import networkx as nx
import matplotlib.pyplot as plt
# Crear el grafo con networkx
G = nx.Graph()

# Añadir los nodos y las aristas del grafo
for node, edges in grafo.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

plt.figure(figsize=(8, 6))
nx.draw(G, coordenadas, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, coordenadas, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.grid(True)
plt.title("Grafo de las cuidades con NetworkX")
plt.show()
