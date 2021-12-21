
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
  
  # def get_neighbors_names(self,vertex_name):
  #       keys = self.__adj_list.keys()
  #       names = []
  #       for key in keys:
  #             if key.value == vertex_name:
  #                   names = self.__adj_list.get(key, [])
  #       if len(names):    
  #         names = [city_name.vertex.value for city_name in names ]           
  #         names.insert(0, vertex_name)
  #       return names
    
        
        
        
  

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
  
    """
  Input : Vertex
  What is doing: Traverse the graph in pre-order depth-first  starting from input vertex
  Return: A list of all visited vertices in pre order
  """
  def depth_first(self, start_vertex):
    if start_vertex not in self.get_nodes():
          raise KeyError("This node not added to the graph")
    stack = []
    result = []
    visited = set()
     
    stack.append(start_vertex)
    while stack:
      current_vertex = stack[-1]
      if current_vertex not in visited:
        visited.add(current_vertex)
        result.append(current_vertex)

      neighbors = self.get_neighbors(current_vertex)
      all_neighbors_visited = True

            
      for edge in neighbors:
          neighbor = edge.vertex
          if neighbor not in visited:
              stack.append(neighbor)
              all_neighbors_visited = False   

              break
      if all_neighbors_visited:
            stack.pop()
    return result

  

if __name__ == "__main__":
      graph = Graph()
      pandora = graph.add_node("Pandora")
      arendelle = graph.add_node("Arendelle")
      metroville = graph.add_node("Metroville")
      monstroplolis = graph.add_node("Monstroplolis")
      narnia = graph.add_node("Narnia")
      naboo = graph.add_node("Naboo")
      
      graph.add_edge(pandora, arendelle,150)
      graph.add_edge(pandora, metroville,82)

      graph.add_edge(arendelle,pandora,150)
      graph.add_edge(arendelle,metroville,99)
      graph.add_edge(arendelle,monstroplolis,42)
      graph.add_edge(metroville,arendelle,99)
      graph.add_edge(metroville,monstroplolis,105)
      graph.add_edge(metroville,pandora,82)
      graph.add_edge(metroville,narnia,37)
      graph.add_edge(metroville,naboo,26)
      graph.add_edge(monstroplolis,arendelle,42)
      graph.add_edge(monstroplolis,metroville,105)
      graph.add_edge(monstroplolis,naboo,73)
      graph.add_edge(narnia,metroville,37)
      graph.add_edge(narnia,naboo,250)
      graph.add_edge(naboo,narnia,250)
      graph.add_edge(naboo,metroville,26)
      graph.add_edge(naboo,monstroplolis,73)
      
      print(graph.breadth_first(pandora))
      print(graph,[metroville,pandora])
      
      graph1 = Graph()
      a =graph1.add_node("A")
      b =graph1.add_node("B")
      c =graph1.add_node("C")
      g = graph1.add_node("G")
      d = graph1.add_node("D")
      e = graph1.add_node("E")
      f = graph1.add_node("F")
      h = graph1.add_node("H")
      
      graph1.add_edge(a,b)
      graph1.add_edge(b,a)
      graph1.add_edge(a,d)
      graph1.add_edge(d,a)
      graph1.add_edge(b,c)
      graph1.add_edge(b,d)
      graph1.add_edge(d,b)
     
      graph1.add_edge(c,b)
      graph1.add_edge(c,g)
      graph1.add_edge(g,c)
      graph1.add_edge(d,e)
      graph1.add_edge(f,d)
      graph1.add_edge(d,h)
      graph1.add_edge(h,d)
     
      graph1.add_edge(e,d)
      graph1.add_edge(d,f)
      graph1.add_edge(f,h)
      graph1.add_edge(h,f)
      
      print(graph1.depth_first(a))


      ## 
      # a = Vertex("a")
      # print(graph.breadth_first(a))









      

