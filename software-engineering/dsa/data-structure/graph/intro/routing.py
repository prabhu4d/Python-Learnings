"""

"""


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def showAllRoutes(self):
        all = []
        for i in self.graph_dict.items():
            print(i)

    def getPaths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.getPaths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    routeGraph = Graph(routes);
    routeGraph.showAllRoutes()

    path = routeGraph.getPaths('Mumbai', 'New York')
    print(path)