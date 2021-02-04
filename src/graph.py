class Node:
  def __init__(self, index):
    self.index = index
    self.value = None
    self.neighbors = None
    self.previous = None
    self.distance = None

class Graph:
  def __init__(self, edges):
    self.edges = edges
    max_index = 0
    for (a,b) in edges:
      if a > max_index:
        max_index = a
      if b > max_index:
        max_index = b
    self.nodes = [Node(i) for i in range(max_index+1)]


  def build_from_edges(self):
    for node in self.nodes:
      neighbor_list = []
      for pair in self.edges:
        if pair[0] == node.index:
          neighbor_list.append(Node(pair[1]))
        if pair[1] == node.index:
          neighbor_list.append(Node(pair[0]))
      node.neighbors = neighbor_list

  def get_nodes_breadth_first(self, starting_index):
    queue = [starting_index]
    visited = []
    while len(visited) != len(self.nodes):
      node = queue[0]
      queue.remove(node)
      visited.append(node)
      for neighbor in [node.index for node in self.nodes[node].neighbors]:
        if neighbor not in visited and neighbor not in queue:
          queue.append(neighbor)
    return [self.nodes[i] for i in visited]

  def get_nodes_depth_first(self, starting_index):
    stack = [starting_index]
    visited = []
    while len(visited) != len(self.nodes):
      node = stack[0]
      stack.remove(node)
      visited.append(node)
      for neighbor in [node.index for node in self.nodes[node].neighbors]:
        if neighbor not in visited and neighbor not in stack:
          stack.insert(0, neighbor)
    return [self.nodes[i] for i in visited]

  def set_breadth_first_distance_and_previous(self, starting_node_index):
    queue = [starting_node_index]
    visited = []
    while len(visited) != len(self.nodes):
      node = queue[0]
      queue.remove(node)
      visited.append(node)
      for neighbor in [node.index for node in self.nodes[node].neighbors]:
        if neighbor not in visited and neighbor not in queue:
          neighbor.previous = node
          node.distance += 1
          queue.append(neighbor)
    return visited

  
  def calc_distance(self, starting_node_index, ending_node_index):
    nodes = self.set_breadth_first_distance_and_previous(starting_node_index)
    return nodes[ending_node_index].distance


