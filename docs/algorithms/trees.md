---
file_format: mystnb
kernelspec:
  name: python3
---

```{title} Tree Data Structure & Algorithms
```

# Tree Data Structure

## Spanning Trees
A spanning tree is a sub-graph of an undirected connected graph, which includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree. The edges may or may not have weights assigned to them.

```{image} https://he-s3.s3.amazonaws.com/media/uploads/146b47a.jpg
:alt: Spanning Tree
:width: 70%
:align: center
```

### Minimum Spanning Tree

A minimum spanning tree is a spanning tree with the minimum possible sum of edge weights. The edges may or may not have weights assigned to them.

```{image} https://he-s3.s3.amazonaws.com/media/uploads/146b47a.jpg
:alt: Minimum Spanning Tree
:width: 70%
:align: center
```
### Finding Minimum Spanning Tree
There are many algorithms to find the minimum spanning tree. The most common ones are:

* Kruskal's Algorithm
* Prim's Algorithm

### Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. If the graph is not connected, then it finds a minimum spanning forest (a minimum spanning tree for each connected component).

Algorithm Steps:

* Sort the graph edges with respect to their weights.
* Start adding edges to the MST from the edge with the smallest weight until the edge of the largest weight.
* Only add edges which doesn't form a cycle , edges which connect only disconnected components.

```{image} https://he-s3.s3.amazonaws.com/media/uploads/6322896.jpg
:alt: Kruskal's Algorithm
:width: 70%
:align: center
```

## Amortized Analysis

Amortized analysis is a method of analyzing the costs associated with a data structure that averages the worst operations out over time.


