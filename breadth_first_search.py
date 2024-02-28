from queue import Queue

graph = {
    1: {2, 3},
    2: {4, 5},
    3: {2, 5},
    4: {5, 6},
    5: {6},
    6: {},
}

start_node = 1
end_node = 6
steps = 0
visited_nodes = []
q = Queue()
q.put(start_node)

while not q.empty():
    current_node = q.get()
    if current_node not in visited_nodes:
        visited_nodes.append(current_node)
        steps += 1
        for n in graph[current_node]:
            if n == end_node:
                print(steps)
        else:
            q.put(n)
