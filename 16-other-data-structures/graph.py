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
