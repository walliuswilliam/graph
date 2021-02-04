class Node:
  def __init__(self, index):
    self.index = index
    self.value = None
    self.neighbors = None
    self.previous = None
    self.distance = None

class Graph:
  def __init__(self, edges, max_index):
    self.edges = edges
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
    return visited

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
    return visited

