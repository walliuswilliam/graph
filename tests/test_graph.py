import sys
sys.path.append('src')
from graph import Graph
from graph import Node

edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
graph = Graph(edges, 5)
graph.build_from_edges()

bf = graph.get_nodes_breadth_first(2)

print('testing breadth first search...')
assert bf == [2, 1, 0, 3, 4, 5], bf
print('passed')


df = graph.get_nodes_depth_first(2)

print('testing depth first search...')
assert df == [2, 1, 4, 5, 3, 0], df
print('passed')