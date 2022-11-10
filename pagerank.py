import networkx as nx
import pylab as plt
D = nx.DiGraph()
n=int(input("\nEnter no.of nodes:"))
for i in range(n):
    print(f"\nEnter Node{i+1}:")
    D.add_weighted_edges_from([(input("Enter Parent:"),input("Enter Child"),int(input("Enter Weight:")))])
    print("\nPage Rank: ",nx.pagerank(D))
nx.draw(D,with_labels=True)
plt.show()
