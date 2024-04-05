def getMinimumMoves(maze, k):
    from collections import deque

    # Directions array considering all the possible 'k' jumps.
    directions = [(x, 0) for x in range(1, k + 1)] + \
                 [(0, x) for x in range(1, k + 1)] + \
                 [(-x, 0) for x in range(1, k + 1)] + \
                 [(0, -x) for x in range(1, k + 1)]

    n = len(maze)  # Number of rows
    m = len(maze[0])  # Number of columns

    # Helper function to check if a move is within bounds and not an obstacle.
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and maze[x][y] == 0

    # Initialize the queue with the starting point (0, 0).
    queue = deque([(0, 0, 0)])  # (x, y, distance)
    visited = set([(0, 0)])

    # Perform BFS.
    while queue:
        x, y, dist = queue.popleft()
        # If the end cell is reached, return the number of moves.
        if x == n - 1 and y == m - 1:
            return dist
        # Check all possible moves.
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, dist + 1))

    # Return -1 if the end cell is not reachable.
    return -1