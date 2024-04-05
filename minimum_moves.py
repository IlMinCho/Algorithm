# def getMinimumMoves(maze, k):
#     from collections import deque

#     # Directions array considering all the possible 'k' jumps.
#     directions = [(x, 0) for x in range(1, k + 1)] + \
#                  [(0, x) for x in range(1, k + 1)] + \
#                  [(-x, 0) for x in range(1, k + 1)] + \
#                  [(0, -x) for x in range(1, k + 1)]

#     n = len(maze)  # Number of rows
#     m = len(maze[0])  # Number of columns

#     # Helper function to check if a move is within bounds and not an obstacle.
#     def is_valid(x, y):
#         return 0 <= x < n and 0 <= y < m and maze[x][y] == 0

#     # Initialize the queue with the starting point (0, 0).
#     queue = deque([(0, 0, 0)])  # (x, y, distance)
#     visited = set([(0, 0)])

#     # Perform BFS.
#     while queue:
#         x, y, dist = queue.popleft()
#         # If the end cell is reached, return the number of moves.
#         if x == n - 1 and y == m - 1:
#             return dist
#         # Check all possible moves.
#         for dx, dy in directions:
#             new_x, new_y = x + dx, y + dy
#             if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
#                 visited.add((new_x, new_y))
#                 queue.append((new_x, new_y, dist + 1))

#     # Return -1 if the end cell is not reachable.
#     return -1

def getMinimumMoves(maze, k):
    from collections import deque

    n = len(maze)  # Number of rows
    m = len(maze[0])  # Number of columns

    # Helper function to check if the cell is within bounds and not an obstacle
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and maze[x][y] == 0

    # Check if there is any obstacle in the straight path between two cells
    def is_path_clear(x1, y1, x2, y2):
        # Vertical move
        if x1 == x2:
            for j in range(min(y1, y2) + 1, max(y1, y2)):
                if maze[x1][j] == 1:
                    return False
        # Horizontal move
        elif y1 == y2:
            for i in range(min(x1, x2) + 1, max(x1, x2)):
                if maze[i][y1] == 1:
                    return False
        return True

    # Initialize the queue with the starting point (0, 0).
    queue = deque([(0, 0, 0)])  # (x, y, distance)
    visited = set([(0, 0)])

    # Perform BFS.
    while queue:
        x, y, dist = queue.popleft()
        # If the end cell is reached, return the number of moves.
        if x == n - 1 and y == m - 1:
            return dist
        # Explore all possible 'k' moves in each direction
        for dx in range(-k, k + 1):
            for dy in range(-k, k + 1):
                # Skip if it's not a straight line move or the move is out of bounds
                if dx != 0 and dy != 0 or not is_valid(x + dx, y + dy):
                    continue
                # If there are obstacles in the path, skip this move
                if not is_path_clear(x, y, x + dx, y + dy):
                    continue
                # If this cell has not been visited yet, add it to the queue
                if (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    queue.append((x + dx, y + dy, dist + 1))

    # If the end cell is not reachable, return -1
    return -1