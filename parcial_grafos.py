import networkx as nx

import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5, 6])

aristas = [
    (1, 3),
    (1, 2),
    (1, 6),
    (3, 5),
    (3, 4),
    (5, 4),
    (4, 2),
    (4, 6)
]

G.add_edges_from(aristas)

posiciones = {
    1: (0, 3),
    2: (2, 2),
    3: (-2, 2),
    4: (0, 1),
    5: (-2, 0),
    6: (2, 0)
}

plt.figure(figsize=(8, 6))

nx.draw(
    G,
    pos=posiciones,
    with_labels=True,
    node_color="steelblue",
    node_size=1200,
    font_size=14,
    font_color="white",
    font_weight="bold",
    edge_color="gray",
    width=2
)

plt.title("Parcial Final - Grafo No Dirigido")

plt.savefig("grafo_parcial.png", dpi=300)

plt.show()

print("Vértices:", list(G.nodes()))
print("Aristas:", list(G.edges()))
print("Cantidad de vértices:", G.number_of_nodes())
print("Cantidad de aristas:", G.number_of_edges())
