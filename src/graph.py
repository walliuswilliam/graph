class Node:
  def __init__(self, index):
    self.index = index
    self.value = None
    self.neighbors = None

class Graph:
  def __init__(self, edges):
    self.edges = edges
    

  def get_neighbors(self, node):
    output_list = []
    for pair in self.edges:
      if pair[0] == node.index:
        output_list.append(Node(pair[1]))
      if pair[1] == node.index:
        output_list.append(Node(pair[0]))
    return output_list

