import sys
sys.path.append('src')
from tree import Tree

edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('g','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('c','k')]
tree = Tree(edges)
tree.build_from_edges()


# print('finding the root...')
# assert tree.root.value == 'e'
# print('passed')

# print('finding children of "root"...')
# assert [node.value for node in tree.root.children] == ['g','i','a']
# print('passed')

# print('finding children of "a"...')
# assert [node.value for node in tree.root.children[2].children] == ['c', 'd']
# print('passed')

# print('finding children of "i"...')
# assert [node.value for node in tree.root.children[1].children] == []
# print('passed')

# print('finding children of "g"...')
# assert [node.value for node in tree.root.children[0].children] == ['b']
# print('passed')

# print('finding children of "c"...')
# assert [node.value for node in tree.root.children[2].children[0].children] == ['k']
# print('passed')

# print('finding children of "d"...')
# assert [node.value for node in tree.root.children[2].children[1].children] == ['f', 'j']
# print('passed')

# print('finding children of "b"...')
# assert [node.value for node in tree.root.children[0].children[0].children] == []
# print('passed')

# print('finding children of "k"...')
# assert [node.value for node in tree.root.children[2].children[0].children[0].children] == []
# print('passed')

# print('finding children of "j"...')
# assert [node.value for node in tree.root.children[2].children[1].children[1].children] == []
# print('passed')

# print('finding children of "f"...')
# assert [node.value for node in tree.root.children[2].children[1].children[0].children] == ['h']
# print('passed')


print('testing nodes_breadth_first...')
nodes = tree.nodes_breadth_first()
assert [node.value for node in nodes] == ['e','g','i','a','b','c','d','k','f','j','h']
print('passed')

print('testing nodes_breadth_first...')
nodes = tree.nodes_breadth_first()
assert [node.value for node in nodes] == ['e','g','i','a','b','c','d','k','f','j','h']
print('passed')