# Initialize a 2D grid (3x3 for example)
grid = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Function to print the grid


def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


# Print the initial grid
print("Initial Grid:")
print_grid(grid)
