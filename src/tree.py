class Node:
  def __init__(self, value):
    self.value = value
    self.children = None

class Tree:
  def __init__(self, edges):
    self.edges = edges
    self.root = self.get_roots(edges)
  
  def build_from_edges(self):
    node_array = [self.root]
    while node_array != []:
      child_array = []
      for node in node_array:
        children = self.get_children(node.value)
        child_array += children
        node.children = children
      node_array = list(child_array)
    
  def get_children(self, parent):
    output_list = []
    for pair in self.edges:
      if pair[0] == parent:
        output_list.append(Node(pair[1]))
    return output_list

  def get_parents(self, child):
    output_list = []
    for pair in self.edges:
      if pair[1] == child:
        output_list.append(Node(pair[0]))
    return output_list

  def get_roots(self, input_list):
    output_list = []
    for pair in input_list:
      if self.get_parents(pair[0]) == []:
        output_list.append(pair[0])
        break
    return Node(output_list[0])

  def nodes_breadth_first(self):
    queue = [self.root]
    visited = []
    while len(queue) != 0:
      node = queue[0]
      queue.remove(node)
      visited.append(node)
      for child in node.children:
        queue.append(child)
    return visited

  # def nodes_depth_first():

