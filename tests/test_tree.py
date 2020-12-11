import sys
sys.path.append('src')
from tree import Tree

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
tree = Tree(edges)
tree.build_from_edges()


assert [node.value for node in tree.root.children] == ['a', 'i', 'g']

assert [node.value for node in tree.root.children[0].children] == ['c', 'd']

assert [node.value for node in tree.root.children[1].children] == []

assert [node.value for node in tree.root.children[2].children] # children of g
['b']

assert [node.value for node in tree.root.children[0].children[0].children] # children of c
['k']

assert [node.value for node in tree.root.children[0].children[1].children] # children of d
['j', 'f']

assert [node.value for node in tree.root.children[2].children[0].children] # children of b
[]

assert [node.value for node in tree.root.children[0].children[0].children[0].children] # children of k
[]

assert [node.value for node in tree.root.children[0].children[1].children[0].children] # children of j
[]

assert [node.value for node in tree.root.children[0].children[1].children[1].children] # children of f
['h']

assert [node.value for node in tree.root.children[0].children[1].children[1].children[0].children] # children of f
[]