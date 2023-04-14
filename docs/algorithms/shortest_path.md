---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Shortest Path Algorithms
```

# Shortest Path Algorithms
The shortest path problem is about finding a path between 2 vertices in a graph such that the total sum of the edges weights is minimum.
This problem could be solved easily using (BFS) if all edge weights were 1.

## Bellman Ford's Algorithm
Bellman Ford's algorithm is a dynamic programming algorithm that solves the shortest path problem in graphs with negative edge weights.
It is a generalization of Dijkstra's algorithm that works on graphs with negative edge weights.

Shortest path contains at most n -1 edges, because the shortest path couldn't have a cycle.

So why shortest path shouldn't have a cycle ?
There is no need to pass a vertex again, because the shortest path to all other vertices could be found without the need for a second visit for any vertices.


### Algorithm Steps:

1. Initialize the distance of all vertices to infinity.
2. Set the distance of the source vertex to 0.
3. Relax all edges n - 1 times.
4. Check for negative-weight cycles.


## Dijkstra's Algorithm
Dijkstra's algorithm is a dynamic programming algorithm that solves the shortest path problem in graphs with non-negative edge weights.
It is a generalization of BFS that works on graphs with non-negative edge weights.

### Basics of Dijkstra's Algorithm
* Dijkstra's Algorithm basically starts at the node that you choose (the source node) and it analyzes the graph to find the shortest path between that node and all the other nodes in the graph.
* The algorithm keeps track of the currently known shortest distance from each node to the source node and it updates these values if it finds a shorter path.
* Once the algorithm has found the shortest path between the source node and another node, that node is marked as "visited" and added to the path.
* The process continues until all the nodes in the graph have been added to the path. This way, we have a path that connects the source node to all other nodes following the shortest path possible to reach each node.

### Requirements
Dijkstra's Algorithm can only work with graphs that have positive weights. This is because, during the process, the weights of the edges have to be added to find the shortest path.

If there is a negative weight in the graph, then the algorithm will not work properly. Once a node has been marked as "visited", the current path to that node is marked as the shortest path to reach that node. And negative weights can alter this if the total weight can be decremented after this step has occurred.