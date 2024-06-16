# 아래 그림과 같은 미로가 있다. 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

# 아래의 예시에서는 도달 가능하다.
 
# 아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.
 
# 위의 예시는 공간상의 이유로 100x100이 아닌 16x16으로 주어졌음에 유의한다.

# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

# 총 10개의 테스트 케이스가 주어진다.

# 테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).

from collections import deque

def bfs(maze, start_x, start_y):
    # 방향 벡터: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start_x, start_y)])
    visited = [[False] * 100 for _ in range(100)]
    visited[start_y][start_x] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치가 도착점이면 True 반환
        if maze[y][x] == 3:
            return True
        
        # 네 방향으로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동 가능한 조건: 미로의 범위 내에 있고, 벽이 아니며, 방문하지 않은 경우
            if 0 <= nx < 100 and 0 <= ny < 100 and maze[ny][nx] != 1 and not visited[ny][nx]:
                queue.append((nx, ny))
                visited[ny][nx] = True
    
    return False

# 테스트 케이스 처리
for _ in range(10):
    tc_num = int(input().strip())
    maze = [list(map(int, input().strip())) for _ in range(100)]
    
    # 출발점 (1, 1)에서 BFS 시작
    result = 1 if bfs(maze, 1, 1) else 0
    
    # 결과 출력
    print(f"#{tc_num} {result}")