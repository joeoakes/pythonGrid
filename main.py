import random

# Function to display the grid
def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * (len(grid) * 4 - 1))  # Adjust separator length dynamically based on grid size

# Create a function to initialize a grid with specified dimensions
def create_grid(rows, cols):
    return [[" " for _ in range(cols)] for _ in range(rows)]

# Set grid dimensions (modifiable)
rows = 10
cols = 10

# Create an empty grid based on the given dimensions
grid = create_grid(rows, cols)

# List of objects to be placed on the grid
objects = [
    "bot",
    "cone",
    "bot",
    "cone",
    "Me",
    "Cone"
]

# Place "lidar" in the middle of the grid
mid_row = rows // 2
mid_col = cols // 2
grid[mid_row][mid_col] = "lidar"

# Track the position already occupied by "lidar"
placed_positions = {(mid_row, mid_col)}

# Randomly place the remaining objects on the grid
for obj in objects:
    while True:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if (row, col) not in placed_positions:  # Ensure no duplicate positions
            grid[row][col] = obj
            placed_positions.add((row, col))
            break

# Display the updated grid
display_grid(grid)
