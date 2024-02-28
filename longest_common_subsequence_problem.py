string1 = "longest"
string2 = "stone"

grid = [[0] * (len(string1) + 1)] * (len(string2) + 1)
# TODO: making a grid without numpy
# TODO: it looks like when a grid is made this way, each row is an alias for
# the same list in memory

for i, l1 in enumerate(string2):
    for j, l2 in enumerate(string1):
        if l1 == l2:
            grid[i + 1][j + 1] = grid[i][j] + 1
        else:
            grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j])

print(grid)
