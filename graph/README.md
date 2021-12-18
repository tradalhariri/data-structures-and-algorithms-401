# Graphs

***A graph is a non-linear data structure that has a finite number of vertices and edges, and these edges are used to connect the vertices. The vertices are used to store the data elements, while the edges represent the relationship***

## Challenge


***Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:***
- add node
> Arguments: value
Returns: The added node
Add a node to the graph

- add edge
> Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
- get nodes
> Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)

- get neighbors
> Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection
- size
> Arguments: none
Returns the total number of nodes in the graph
## Approach & Efficiency
> Add Node

**Time : O(1).**

**Space : O(1).**

> Add Edge

**Time : O(1).**

**Space : O(1).**

> Get Nodes

**Time: O(n).**

**Space: O(1).**

> Get Neighbors

**Time: O(n).**

**Space: O(1).**

> Size:

**Time: O(1).**

**Space: O(1).**

## API
> Add Node : add new node to the graph
> Add Edge : add edge between two nodes in the graph
> Get Nodes : return all nodes in the graph as list
> Get Neighbors return all neighbors in the graph as list
> Size: return the count of nodes in the graph