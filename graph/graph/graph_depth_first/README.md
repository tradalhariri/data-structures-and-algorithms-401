
# Depth First Traversal
> Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
## Challenge
> You should extend the graph implementation and add a method called
Name: Depth first
Arguments: Node (Starting point of search)
Return: A collection of nodes in their pre-order depth-first traversal order
Program output: Display the collection

## Approach & Efficiency

***Algorithm***
- Define  a method called depth_first that takes a node as parameter.
- Push the  node into the stack.
- Start a while loop while the stack is not empty.
- Peek at the top node in the stack.
- If the top node has unvisited children, mark the top node as visited, and then Push any unvisited children back into the stack
- If the top node does not have any unvisited children, Pop that node off the stack.
- repeat until the stack is empty.
- return the result


***Time Complexity*** is O(N^2) because the worst case is when the graph is complete then for each node in the graph we need to check if the neighbors were visited or not

***Space Complexity*** is O(N) because of the needing for stack and set and list
## Solution
![](graph_depth_first.jpg)

## Requirements
1. [unit tests](../../tests/test_graph.py){:target="_blank"}
2. [README](../graph_depth_first/README.md){:target="_blank"}
3. [submisstion](../../graph/graph.py){:target="_blank"}
