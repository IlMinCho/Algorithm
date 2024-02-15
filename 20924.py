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


from collections import defaultdict

# 입력 처리
n, root = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n-1)]

# 인접 리스트 생성
graph = defaultdict(list)
for a, b, d in edges:
    graph[a].append((b, d))
    graph[b].append((a, d))

# 스택을 사용한 반복적 DFS로 기둥과 가지의 길이 계산
def iterative_dfs(root, graph):
    stack = [(root, 0, False)]  # (노드, 현재까지의 길이, 기가 노드 여부)
    visited = set()
    pillar_length = 0
    longest_branch_length = 0
    giga_node_found = False

    while stack:
        node, length, is_giga = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if not giga_node_found and (len(graph[node]) > 2 or (node == root and len(graph[node]) > 1)):
            giga_node_found = True
            pillar_length = length
            is_giga = True  # 현재 노드를 기가 노드로 설정

        elif len(graph[node]) == 1 and node != root:  # 리프 노드
            if giga_node_found:  # 기가 노드 이후의 리프 노드
                longest_branch_length = max(longest_branch_length, length - pillar_length)

        for next_node, dist in graph[node]:
            if next_node not in visited:
                stack.append((next_node, length + dist, is_giga))

    return pillar_length, longest_branch_length

pillar_length, longest_branch_length = iterative_dfs(root, graph)
print(pillar_length, longest_branch_length)
