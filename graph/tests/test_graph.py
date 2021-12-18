from graph import __version__
from graph.graph import Graph,Vertex,Edge

import pytest

def test_version():
    assert __version__ == '0.1.0'
    

# Node can be successfully added to the graph

def test_graph_can_add_node(graph):
    c = graph.add_node("c")
    assert c in graph.get_nodes()
    
    
# An edge can be successfully added to the graph
def test_graph_can_add_edge():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a,b)
    assert isinstance(graph.get_neighbors(a)[0], Edge)
# A collection of all nodes can be properly retrieved from the graph
def test_graph_can_retreive_all_nodes():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    assert graph.get_nodes() == [a, b]

# All appropriate neighbors can be retrieved from the graph
def test_graph_can_retreive_all_neighbors():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    graph.add_edge(a,b)
    graph.add_edge(a,c)
    
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 2
    neighbor_edge_b = neighbors[0]
    neighbor_edge_c = neighbors[1]
    assert neighbor_edge_b.vertex.value == 'b'
    
    assert neighbor_edge_c.vertex.value == 'c'
    
# Neighbors are returned with the weight between nodes included
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    graph.add_edge(a,b,25)
    graph.add_edge(a,c)
    
    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 2
    neighbor_edge_b = neighbors[0]
    neighbor_edge_c = neighbors[1]
    assert neighbor_edge_b.vertex.value == 'b'
    assert neighbor_edge_b.weight == 25
    assert neighbor_edge_c.vertex.value == 'c'
    assert neighbor_edge_c.weight == 1


# The proper size is returned, representing the number of nodes in the graph

def test_size(graph):
    return graph.size == 2
    
# A graph with only one node and edge can be properly returned
def test_graph_with_only_one_node_and_edge():
    graph = Graph()

    a = graph.add_node('a')
    graph.add_edge(a, a, 1)

    neighbors = graph.get_neighbors(a)
    assert len(neighbors) == 1
    neighbor_edge_a = neighbors[0]
    
    assert neighbor_edge_a.vertex.value == 'a'
    assert neighbor_edge_a.weight == 1

# An empty graph properly returns null

def test_empty_graph():
    graph = Graph()
    assert graph.get_adj_list() == {}


@pytest.fixture
def graph():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    return graph

