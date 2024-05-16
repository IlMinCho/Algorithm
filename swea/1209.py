# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# 다음과 같은 5X5 배열에서 최댓값은 29이다.

# [제약 사항]

# 총 10개의 테스트 케이스가 주어진다.

# 배열의 크기는 100X100으로 동일하다.

# 각 행의 합은 integer 범위를 넘어가지 않는다.

# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
# [입력]

# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

def max_sum_in_grid(grid):
    size = len(grid)
    
    max_sum = 0
    
    # 행의 합 계산
    for row in grid:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
    
    # 열의 합 계산
    for col in range(size):
        col_sum = sum(grid[row][col] for row in range(size))
        if col_sum > max_sum:
            max_sum = col_sum
    
    # 주요 대각선의 합 계산
    diag1_sum = sum(grid[i][i] for i in range(size))
    if diag1_sum > max_sum:
        max_sum = diag1_sum
    
    # 부 대각선의 합 계산
    diag2_sum = sum(grid[i][size - 1 - i] for i in range(size))
    if diag2_sum > max_sum:
        max_sum = diag2_sum
    
    return max_sum

# 외부 입력 받기
test_cases = 10
results = []

for tc in range(1, test_cases + 1):
    _ = input()  # 테스트 케이스 번호를 읽기 (사용하지 않음)
    grid = [list(map(int, input().split())) for _ in range(100)]
    
    result = max_sum_in_grid(grid)
    results.append(f"#{tc} {result}")

# 결과 출력
for result in results:
    print(result)