import networkx as nx

import matplotlib.pyplot as plt


# G = nx.DiGraph()
k = nx.lollipop_graph(4, 30)
poos = nx.circular_layout(k)
# G.add_edge("1","2")
# G.add_edge("1","3")
# G.add_edge("1","4")
# G.add_edge("1","5")
# G.add_edge("1","6")
# pos = nx.circular_layout(G,dim=2,scale=3)
# poos = nx.spring_layout(G, iterations=100)
# print (nx.info(G))
# nx.draw(G,pos, node_size=800)
nx.draw(k,poos, node_size=800)
plt.show()
