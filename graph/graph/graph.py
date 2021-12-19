
from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)
  
  def dequeue(self):
    return self.dq.popleft()
  
  def __len__(self):
    return len(self.dq)

class Vertex:
  """
  Input:Value
  What is doing: Store the value
  Return: None
  """
  def __init__(self, value):
      self.value = value

  def __str__(self):
      return self.value
    
  def __repr__(self):
      return self.value


class Edge:
  """
  Input: Vertex, weight
  What is doing: Store the vertex and the weight
  Return: None
  """
  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight
    
  def __str__(self):
        return f"{self.vertex.value}:{self.weight}"
      
  def __repr__(self):
        return f"{self.vertex.value}:{self.weight}"
        
    

class Graph:
  """
  Input: None
  What is doing: It is creating an empty graph 
  Return: None
  """
  def __init__(self):
    self.__adj_list = {}
    
  def get_adj_list(self):
        return self.__adj_list
  """
  Input : Value
  What is doing : add node to the Graph
  Return : node
  """
  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node] = []
    return node

  """
  Input: start_vertex, end_vertex , weight:optional
  What is doing: Creat an edge and append the edge to the value of
  start_vertex inside the adj_list
  Return: None
  """
  def add_edge(self, start_vertex, end_vertex, weight=1):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("End Vertex is not found")
    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)
    
  """
  Input : Vertex
  What is doing: Get all neighbors for a vertex
  Return: a list of edges
  """
  def get_neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])
  
  

  """
  Input : None
  What is doing : get all the nodes in the graph as a set or list
  Return : a list or set of the nodes
  """
  def get_nodes(self):
    return list(self.__adj_list.keys())

  """
  Input: None
  What is doing: find the length of the adj_list
  Return: int The size(the length of adj_list)
  """
  def size(self):
    return len(self.__adj_list)
  """
  Input : Vertex
  What is doing: Traverse the graph level by level (Breadth First) starting from input vertex
  Return: A list of all visited vertices maitaining the level order.
  """
  def breadth_first(self, start_vertex):
    if start_vertex not in self.get_nodes():
          raise KeyError("This node not added to the graph")
    queue = Queue()
    result = []
    visited = set()
     
    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    result.append(start_vertex)

    while len(queue):
      current_vertex = queue.dequeue()

      neighbors = self.get_neighbors(current_vertex)

      for edge in neighbors:
        neighbor = edge.vertex

        if neighbor not in visited:
          queue.enqueue(neighbor)
          visited.add(neighbor)
          result.append(neighbor)

    return result
  

if __name__ == "__main__":
      graph = Graph()
      pandora = graph.add_node("Pandora")
      arendelle = graph.add_node("Arendelle")
      metroville = graph.add_node("Metroville")
      monstroplolis = graph.add_node("Monstroplolis")
      narnia = graph.add_node("Narnia")
      naboo = graph.add_node("Naboo")
      
      graph.add_edge(pandora, arendelle)
      graph.add_edge(arendelle,pandora)
      graph.add_edge(arendelle,metroville)
      graph.add_edge(arendelle,monstroplolis)
      graph.add_edge(metroville,arendelle)
      graph.add_edge(metroville,monstroplolis)
      graph.add_edge(metroville,narnia)
      graph.add_edge(metroville,naboo)
      graph.add_edge(monstroplolis,arendelle)
      graph.add_edge(monstroplolis,metroville)
      graph.add_edge(monstroplolis,naboo)
      graph.add_edge(narnia,metroville)
      graph.add_edge(narnia,naboo)
      graph.add_edge(naboo,narnia)
      graph.add_edge(naboo,metroville)
      graph.add_edge(naboo,monstroplolis)
      
      print(graph.breadth_first(pandora))
      
      ## 
      # a = Vertex("a")
      # print(graph.breadth_first(a))









      

