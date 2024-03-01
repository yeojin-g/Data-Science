import matplotlib.pyplot as plt
import networkx as nx

graph = nx.Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("D", "C")
graph.add_edge("D", "E")
graph.add_edge("A", "E")
graph.add_edge("B", "E")

pos = {"A": (1,10), "B": (2,20), "C": (10,2), "D":(10,5), "E":(7, 13)}
#pos = nx.spring_layout(graph)

nx.draw(graph, pos, with_labels=True)
plt.show()