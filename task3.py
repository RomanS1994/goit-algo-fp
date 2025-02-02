import heapq

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):

        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Для неорієнтованого графа

    def dijkstra(self, start):

        min_heap = [(0, start)]  # (вага, вершина)
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Створення графа
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('D', 'E', 8)
graph.add_edge('E', 'A', 7)

# Виконання алгоритму Дейкстри від вершини 'A'
shortest_paths = graph.dijkstra('A')


print("Найкоротші відстані від A:")
for node, distance in shortest_paths.items():
    print(f"До {node}: {distance}")
