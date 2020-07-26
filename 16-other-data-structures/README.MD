# Other Data Structures

## Graphs

> A graph are networks consisting of nodes or vertices which may or may not be connected to each other. The lines or the path that connects two nodes is called an edge. If the edge has a particular direction of flow, then it is a directed graph, with the direction edge being called an arc. Else if no directions are specified, the graph is called an undirected graph.
<br>
datacamp.com

```py
graph = {"Alfie": ["Tom", "John"],
         "Tom": ["Jerry"],
         "John": ["Alfie", "Jerry"]
         }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))
```

```bash
[('Alfie', 'Tom'), ('Alfie', 'John'), ('Tom', 'Jerry'), ('John', 'Alfie'), ('John', 'Jerry')]
```

<br>

## Tree
Tree can be structured using a combination of other data structures.

<br>

## Files
```File``` refers to data stored in computer.
