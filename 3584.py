# https://www.acmicpc.net/problem/3584

# 가장 가까운 공통 조상

# 문제
# 루트가 있는 트리(rooted tree)가 주어지고, 그 트리 상의 두 정점이 주어질 때 그들의 가장 가까운 공통 조상(Nearest Common Anscestor)은 다음과 같이 정의됩니다.

# 두 노드의 가장 가까운 공통 조상은, 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드를 말합니다.
# nca.png

# 예를 들어  15와 11를 모두 자손으로 갖는 노드는 4와 8이 있지만, 그 중 깊이가 가장 깊은(15와 11에 가장 가까운) 노드는 4 이므로 가장 가까운 공통 조상은 4가 됩니다.

# 루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요

# 입력
# 첫 줄에 테스트 케이스의 개수 T가 주어집니다.

# 각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N이 주어집니다. (2 ≤ N ≤ 10,000)

# 그리고 그 다음 N-1개의 줄에 트리를 구성하는 간선 정보가 주어집니다. 한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻입니다. (당연히 정점이 N개인 트리는 항상 N-1개의 간선으로 이루어집니다!) A와 B는 1 이상 N 이하의 정수로 이름 붙여집니다.

# 테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.

# 출력
# 각 테스트 케이스 별로, 첫 줄에 입력에서 주어진 두 노드의 가장 가까운 공통 조상을 출력합니다.
# import sys

# sys.setrecursionlimit(100000)

# def dfs(tree, node, parent, depth, up):
#     depth[node] = depth[parent] + 1
#     up[node][0] = parent
#     for i in range(1, len(up[node])):
#         up[node][i] = up[up[node][i-1]][i-1]

#     for child in tree[node]:
#         if child != parent:
#             dfs(tree, child, node, depth, up)

# def lca(u, v, depth, up):
#     if depth[u] < depth[v]:
#         u, v = v, u

#     for i in reversed(range(len(up[u]))):
#         if depth[u] - (1 << i) >= depth[v]:
#             u = up[u][i]

#     if u == v:
#         return u

#     for i in reversed(range(len(up[u]))):
#         if up[u][i] != up[v][i]:
#             u = up[u][i]
#             v = up[v][i]

#     return up[u][0]

# def preprocess_and_solve(n, edges, queries):
#     tree = [[] for _ in range(n + 1)]
#     for u, v in edges:
#         tree[u].append(v)
#         tree[v].append(u)

#     depth = [0] * (n + 1)
#     up = [[0] * n.bit_length() for _ in range(n + 1)]
#     dfs(tree, 1, 0, depth, up)

#     return [lca(u, v, depth, up) for u, v in queries]

# if __name__ == "__main__":
#     T = int(input())
#     for _ in range(T):
#         N = int(input())
#         edges = []
#         for _ in range(N - 1):
#             u, v = map(int, input().split())
#             edges.append((u, v))
#         u, v = map(int, input().split())
#         queries = [(u, v)]
#         result = preprocess_and_solve(N, edges, queries)
#         print(result[0])

def find_parent(parent, x):
    parents = []
    while x:
        parents.append(x)
        x = parent[x]
    return parents

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        parent = [0] * (N + 1)  # 각 노드의 부모 노드를 저장하는 리스트, 0번 인덱스는 사용하지 않음

        # 간선 정보 입력받아 부모 노드 설정
        for _ in range(N - 1):
            u, v = map(int, input().split())
            parent[v] = u

        x, y = map(int, input().split())
        
        # 부모 리스트를 거꾸로 탐색하여 깊이가 0인 부모까지 기록
        x_parents = find_parent(parent, x)
        y_parents = find_parent(parent, y)

        # 깊이 맞추기
        i = len(x_parents) - 1
        j = len(y_parents) - 1

        # 최소 공통 조상 찾기
        lca = 0
        while i >= 0 and j >= 0 and x_parents[i] == y_parents[j]:
            lca = x_parents[i]
            i -= 1
            j -= 1

        print(lca)