class Graph:

    def __init__(self) -> None:
        self.adj_matrix = [
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0]
            ]

    def bfs(self) -> list:
        pass
    

if __name__ == "__main__":
    g = Graph()