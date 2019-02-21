# Connected Components in Apache Spark



### Objective
The task in this assignment is to implement efficient end-to-end Apache Spark program for finding connected components. There are several assumptions:

Undirected graph on which we are operating is too large to be represented in the memory of a single compute node.

The graph is represented by a list of edges in the form source target, where source is integer representing source vertex id, target is integer representing target vertex id, and source and target are separated with single space.

Graph has no self-loops (i.e. source = target) and no particular ordering of source, target is assumed.


### Description
Given a graph, this algorithm identifies the [connected components](https://en.wikipedia.org/wiki/Connected_component_(graph_theory)) using Apache Spark framework.

In the following, a connected component will be called as "cluster".

The algorithm tries to implement the "The Two-Phase Algorithm" proposed in the paper [Connected Components in MapReduce and Beyond](http://dl.acm.org/citation.cfm?id=2670997). Below is the pseudo-code of the algorithm.

              1: **Input:** Edges (u, v) as a set of key-value pairs <u; v>.
              2: **Input:** A unique label lv for every node v ∈ V .
              3: **repeat**
              4:    **repeat**
              5:        Large-Star
              6:    **until** Convergence
              7:    Small-Star
              8: **until** Convergence


The application takes one input command line argument: the name of a file or directory containing the graph to analyze. You may assume that input is always correct and input files are passed properly.

The application creates a folder or file, with output in the form vertex label, where vertex is vertex id, and label is the label of connected component to which vertex belongs. Vertex and label is by a white space.
