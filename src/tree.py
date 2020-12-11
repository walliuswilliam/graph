class Node:
  def __init__(self, data):
    self.data = data
    self.children = None

class Tree:
  def __init__(self, edges):
    self.edges = edges
    self.root = self.get_roots(edges)
  
  def build_from_edges(self):
    node_array = [self.root]
    while node_array != None:
      child_array = []
      for node in node_array:
        

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
    return output_list
