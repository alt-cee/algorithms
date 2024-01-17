import queue

class Graph:

    def __init__(self) -> None:
        self.adj_matrix = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0]
            ]

    def bfs(self, node) -> list:
        q = queue.Queue()
        visited = []
        q.put(node)
        
        while not q.empty():
            current_node = q.get()
            if current_node not in visited:
                visited.append(current_node)
                for i, n in enumerate(self.adj_matrix[current_node]):
                    if n == 1 and (i not in visited):
                        q.put(i)

        return visited
    

if __name__ == "__main__":
    g = Graph()
    print("BFS starting from node 1: ", g.bfs(1))
    print("BFS starting from node 7: ", g.bfs(7))