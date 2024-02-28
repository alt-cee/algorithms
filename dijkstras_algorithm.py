graph = {
    1: {2: 5, 3: 2},
    2: {4: 4, 5: 2},
    3: {2: 8, 5: 7},
    4: {5: 6, 6: 3},
    5: {6: 1},
    6: {},
}

max_edge_weight = 10
parent = {2: 1, 3: 1}  # TODO: go over different ways to enter values into a dict
cost = {2: 5, 3: 2, 4: max_edge_weight, 5: max_edge_weight, 6: max_edge_weight}
visited_nodes = [1]
start_node = 1
end_node = 6
# TODO: handle first step of the algorithm (initialization)


def get_closest_unvisited_node(cost):
    # TODO: getting key out of dict based on min. value
    min_cost = 10
    closest_node = None
    for node in cost:
        # TODO: review dict iteration
        if (node not in visited_nodes) and (cost[node] < min_cost):
            min_cost = cost[node]
            closest_node = node
    return closest_node


# TODO: handle variable scope
# TODO: create a function to handle running algorithm
while len(visited_nodes) < len(graph.keys()):
    node = get_closest_unvisited_node(cost)
    for neighbor in graph[node]:
        current_cost = cost[neighbor]
        update_cost = cost[node] + graph[node][neighbor]
        if update_cost < current_cost:
            cost[neighbor] = update_cost
            parent[neighbor] = node
    visited_nodes.append(node)


print(cost[end_node])
