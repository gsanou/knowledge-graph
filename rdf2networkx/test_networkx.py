import networkx as nx
import matplotlib.pyplot as plt
import rdflib
import pylab

G = nx.DiGraph()
G.add_node(1,name = "111")
G.add_node(2,name = "222")


# print(G.has_node(a))
dict = {1:2}
if(1 in dict):
    print(dict[1])
else:
    print("ssssss")
