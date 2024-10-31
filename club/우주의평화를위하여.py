# A행성에 -> NxN의 격자판에 모든기계의 위치에 나타낼수있다.
# 격자판위의 모든 기계가 같은 종류일시 한번의 공격으로 모든 기계 파괴가능
# 격자판위에 단 하나라도 다른종류의 기계가 있다면, 4개의 구획으로 나누어서 다시 기계를 확인한다.
# 모든 기계 파괴할떄까지 2 ~ 3 단계 나누어서 진행할것
# A 행성의 모든 기계를 파괴하고자한다. 이떄 최소 기계를 몇번이나 동작시켜야 모든 기계를 파괴할수있을까

# 입력 
# 첫번째 줄에는 N, 격자판의 크기주어짐
# N은 항상 2^k형태로 주어진다.
# 두번쨰 줄부터는 NxN 크기에 격자판에 놓여진 기계의 번호가 공백으로 구분되어 주어진다. 기계번호는 항상 0에서 3이하의 자연수

# 출력
# 기계 최소 작동회수를 출력한다.

# 구획이란 하나의 섹션의 벽이라고 생각하면됨 -> 4구획 십자가형태
# N이 홀수면 어려워짐 하지만 짝수로 제한
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def recursion(grid, x, y, N):
    first_value = grid[y][x]
    flag = True
    for i in range(y, y + N):
        for j in range(x, x + N):
            if grid[i][j] != first_value:
                flag = False
                break
        if not flag:
            break
    if flag:
        return 1
    else:
        hn = N // 2
        return (
            recursion(grid, x, y, hn) +               
            recursion(grid, x + hn, y, hn) +        
            recursion(grid, x, y + hn, hn) +         
            recursion(grid, x + hn, y + hn, hn)    
        )

print(recursion(grid, 0, 0, N))

# recursion 
# 2 2 
# 2 2

# 2 2 2 2 
# 2 2 2 2
# 2 2 2 2
# 2 2 2 2



















