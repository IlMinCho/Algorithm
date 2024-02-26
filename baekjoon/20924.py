# https://www.acmicpc.net/problem/20924

# 트리의 기둥과 가지

# 문제


# 시청 공무원 마이크로는 과장으로부터 시에 있는 나무의 기둥의 길이와 가장 긴 가지의 길이를 파악하라는 업무 지시를 받았다.

# 마이크로는 ICPC Sinchon Winter Algorithm Camp에서 배운 트리 자료 구조를 이용하면 이 작업을 좀 더 수월하게 할 수 있으리라 판단했다. 



# 마이크로는 트리의 기둥과 가지를 분류하기 위해 기가 노드를 추가로 정의하였다.

# 기가 노드는 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 
# $2$개 이상인 노드다. 기둥-가지를 줄여 기가 노드라 이름 붙였다. 위 그림에서 기가 노드는 
# $4$번 노드다.



# 단, 위 그림과 같이 리프 노드가 단 
# $1$개인 경우 리프 노드가 동시에 기가 노드가 된다.



# 또한, 위 그림과 같이 루트 노드가 동시에 기가 노드인 경우도 가능하다.



# 트리의 기둥은 루트 노드에서부터 기가 노드까지다. 위 그림에서 기둥은 
# $1-2-3-4$ 이다.
# 기둥의 길이는 기둥의 간선 길이의 합인 
# $1 + 2 + 3 = 6$ 이 된다.
# 트리의 가지는 기가 노드에서부터 임의의 리프 노드까지다. 위 그림에서 가지는 
# $4-5-6-7$, 
# $4-5-8$, 
# $4-9$, 
# $4-10-11$, 
# $4-10-12$ 총 
# $5$개가 있다.
# 가지의 길이는 가지의 간선 길이의 합이다. 다행히도 가장 긴 가지의 길이 하나만 기재하면 된다. 
# $4-10-12$ 가지가 간선 길이의 합 
# $3 + 3 = 6$ 으로 가장 긴 가지이다.
# 마이크로는 시의 나무를 트리 자료 구조로 옮겼다. 그런데 과장이 마이크로에게 또 다른 업무를 지시했다! 너무 바쁜 마이크로를 대신해 트리의 기둥과 가장 긴 가지의 길이를 측정하자.

# 입력
# 첫 번째 줄에는 노드의 개수 
# $N$(
# $1 \le N \le 200\,000$)과 루트 노드의 번호 
# $R$(
# $1 \le R \le N$)이 주어진다.

# 이후 
# $N-1$개의 줄에 세 개의 정수 
# $a$, 
# $b$, 
# $d$(
# $1 \le a, b \le N$, 
# $ a \ne b$)가 주어진다. 이는 
# $a$번 노드와 
# $b$번 노드가 연결되어있으며 이 간선의 길이가 
# $d$(
# $1 \le d \le 1\,000$)임을 의미한다. 노드는 
# $1$번부터 
# $N$번까지 정수 번호가 매겨져 있으며 같은 간선은 여러 번 주어지지 않는다. 

# 트리가 아닌 그래프는 입력으로 주어지지 않는다.

# 출력
# 나무의 기둥의 길이와 가장 긴 가지의 길이를 출력한다.


# from sys import stdin, setrecursionlimit
# from collections import defaultdict
# setrecursionlimit(10**9)

# def get_maxbranch(tree, root):
#     if root not in tree : return 0

#     maxbranch = 0
#     for node, w in tree[root].items():
#         del tree[node][root]
#         branch = w + get_maxbranch(tree, node)
#         if branch > maxbranch :
#             maxbranch = branch
#     return maxbranch

# # 변수초기화
# N, R = map(int, stdin.readline().split())
# tree = defaultdict(dict)
# for _ in range(N-1):
#     a, b, w = map(int, stdin.readline().split())
#     tree[a][b] = w
#     tree[b][a] = w

# # 기가노드까지의 기둥 길이 찾기
# giganode = R
# gigalen = 0
# while len(tree[giganode])==1:
#     node, w = list(tree[giganode].items())[0]
#     del tree[node][giganode]
#     gigalen += w
#     giganode = node

# # 가장 긴 가지 길이 찾기
# maxbranch = get_maxbranch(tree, giganode)

# print('{} {}'.format(gigalen, maxbranch))
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r = map(int, input().split())
graph = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 결과를 저장할 변수: 기둥의 길이, 가장 긴 가지의 길이
ans = [0, 0]

def dfs(node, parent, length, flag):
    global ans
    # 기가 노드 찾기 전: 기둥 길이 계산
    if flag == 0:
        ans[0] = length
    # 기가 노드 찾은 후: 가장 긴 가지의 길이 계산
    else:
        ans[1] = max(ans[1], length)
    
    # 기가 노드 판별
    if flag == 0 and len(graph[node]) > 2 - int(node == r):
        flag, length = 1, 0  # 기가 노드를 찾았으므로 flag 업데이트, 길이 초기화

    for next_node, weight in graph[node]:
        if next_node == parent:
            continue
        dfs(next_node, node, length + weight, flag)

# DFS 실행
dfs(r, -1, 0, 0)

# 결과 출력
print(ans[0], ans[1])