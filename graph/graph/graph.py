
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

