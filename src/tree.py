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
    print('root', self.root.value)
    print('node_array', [n.value for n in node_array])
    for num in range(5): #node_array != []:
      child_array = []
      print('child array', child_array)
      for node in node_array:
        print('node', node.value)
        children = self.get_children(node.value)
        print('children', children)
        child_array += children
      node_array = list(child_array)
    
  def get_children(self, parent):
    output_list = []
    for pair in self.edges:
      if pair[0] == parent:
        output_list.append(pair[1])
    return output_list

  def get_parents(self, child):
    output_list = []
    for pair in self.edges:
      if pair[1] == child:
        output_list.append(pair[0])
    return output_list

  def get_roots(self, input_list):
    output_list = []
    for pair in input_list:
      if self.get_parents(pair[0]) == []:
        output_list.append(pair[0])
        break
    return Node(output_list[0])
