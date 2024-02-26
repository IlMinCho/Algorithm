# https://www.acmicpc.net/problem/2250

# 트리의 높이와 너비

# 문제
# 이진트리를 다음의 규칙에 따라 행과 열에 번호가 붙어있는 격자 모양의 틀 속에 그리려고 한다. 이때 다음의 규칙에 따라 그리려고 한다.

# 이진트리에서 같은 레벨(level)에 있는 노드는 같은 행에 위치한다.
# 한 열에는 한 노드만 존재한다.
# 임의의 노드의 왼쪽 부트리(left subtree)에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고, 오른쪽 부트리(right subtree)에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.
# 노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.
# 이와 같은 규칙에 따라 이진트리를 그릴 때 각 레벨의 너비는 그 레벨에 할당된 노드 중 가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다. 트리의 레벨은 가장 위쪽에 있는 루트 노드가 1이고 아래로 1씩 증가한다.

# 아래 그림은 어떤 이진트리를 위의 규칙에 따라 그려 본 것이다. 첫 번째 레벨의 너비는 1, 두 번째 레벨의 너비는 13, 3번째, 4번째 레벨의 너비는 각각 18이고, 5번째 레벨의 너비는 13이며, 그리고 6번째 레벨의 너비는 12이다.



# 우리는 주어진 이진트리를 위의 규칙에 따라 그릴 때에 너비가 가장 넓은 레벨과 그 레벨의 너비를 계산하려고 한다. 위의 그림의 예에서 너비가 가장 넓은 레벨은 3번째와 4번째로 그 너비는 18이다. 너비가 가장 넓은 레벨이 두 개 이상 있을 때는 번호가 작은 레벨을 답으로 한다. 그러므로 이 예에 대한 답은 레벨은 3이고, 너비는 18이다.

# 임의의 이진트리가 입력으로 주어질 때 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)이 주어진다. 다음 N개의 줄에는 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호가 순서대로 주어진다. 노드들의 번호는 1부터 N까지이며, 자식이 없는 경우에는 자식 노드의 번호에 -1이 주어진다.

# 출력
# 첫째 줄에 너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력한다. 너비가 가장 넓은 레벨이 두 개 이상 있을 때에는 번호가 작은 레벨을 출력한다.
# from collections import deque

# class Node:
#     def __init__(self, number):
#         self.number = number
#         self.left = None
#         self.right = None

# def in_order_traversal(node, order):
#     if node.left:
#         in_order_traversal(node.left, order)
#     order.append(node.number)
#     if node.right:
#         in_order_traversal(node.right, order)

# def bfs(root, column_order):
#     queue = deque([(root, 1)])
#     level_min_max = {}
#     while queue:
#         node, level = queue.popleft()
#         index = column_order.index(node.number)
#         if level in level_min_max:
#             level_min_max[level] = (min(level_min_max[level][0], index), max(level_min_max[level][1], index))
#         else:
#             level_min_max[level] = (index, index)
#         if node.left:
#             queue.append((node.left, level + 1))
#         if node.right:
#             queue.append((node.right, level + 1))
#     return level_min_max

# n = int(input())  # Number of nodes
# nodes = {i: Node(i) for i in range(1, n + 1)}

# root = None
# for _ in range(n):
#     number, left, right = map(int, input().split())
#     if left != -1:
#         nodes[number].left = nodes[left]
#     if right != -1:
#         nodes[number].right = nodes[right]
#     if root is None:
#         root = nodes[number]

# # Find the actual root
# for i in range(1, n + 1):
#     if all(i != child.number for node in nodes.values() for child in [node.left, node.right] if child):
#         root = nodes[i]
#         break

# # In-order traversal to get column order
# column_order = [0]  # Start indexing from 1
# in_order_traversal(root, column_order)
# column_order = [0] + column_order  # Adjusting for 1-based indexing

# # BFS to calculate width of each level
# level_min_max = bfs(root, column_order)

# # Find the level with the maximum width
# max_width = 0
# max_level = 0
# for level, (min_index, max_index) in level_min_max.items():
#     width = max_index - min_index + 1
#     if width > max_width:
#         max_width = width
#         max_level = level

# print(max_level, max_width)




# 기존 코드의 주된 문제점은 bfs 함수 내에서 column_order.index(node.number)를 사용하여 각 노드의 열 인덱스를 찾는 과정에서 비효율이 발생하는 것이었습니다. 이 작업은 리스트 전체를 매번 순회하며 인덱스를 찾기 때문에, 많은 시간이 소요됩니다. 특히, 노드의 수가 많을 때 이로 인한 시간 초과가 발생할 수 있습니다.

# 개선한 코드에서는 이 문제를 해결하기 위해 다음과 같은 접근 방식을 취했습니다:

# 노드 번호와 열 인덱스의 매핑(dictionary 사용): 중위 순회를 수행하면서 각 노드 번호에 대한 열 인덱스를 사전(dictionary)에 저장합니다. 이렇게 하면 나중에 각 노드에 대한 열 인덱스를 O(1) 시간 복잡도로 즉시 찾을 수 있습니다. 이는 node_to_index[node.number]를 통해 이루어집니다.
# node_to_index = {}  # 노드 번호와 열 인덱스의 매핑
# in_order_traversal(root, column_order, node_to_index)
# 루트 노드 찾기 개선: 모든 노드를 순회하여 루트 노드를 찾는 대신, 루트가 될 수 없는 노드(다른 노드의 자식이 되는 노드)를 기록합니다. 그 후, 전체 노드 집합에서 이 노드들을 제외한 나머지 노드를 루트 노드로 결정합니다. 이는 집합 연산을 통해 효율적으로 수행됩니다.
# not_root = set()  # 루트가 될 수 없는 노드의 집합
# for _ in range(n):
#     number, left, right = map(int, input().split())
#     # left와 right를 not_root에 추가
# root_number = (set(nodes.keys()) - not_root).pop()  # 루트 노드 번호 찾기
# root = nodes[root_number]
# BFS를 통한 레벨별 최소 및 최대 열 인덱스 계산: BFS를 사용하여 각 노드의 레벨별로 최소 및 최대 열 인덱스를 계산하고, 이를 바탕으로 각 레벨의 너비를 구합니다. node_to_index 매핑을 통해 각 노드의 열 인덱스를 빠르게 찾을 수 있어, 이 과정이 효율적으로 이루어집니다.
# level_min_max = bfs(root, node_to_index)

from collections import deque

class Node:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None

def in_order_traversal(node, order, node_to_index):
    if node.left:
        in_order_traversal(node.left, order, node_to_index)
    order.append(node.number)
    node_to_index[node.number] = len(order)  # 현재 노드의 인덱스를 저장
    if node.right:
        in_order_traversal(node.right, order, node_to_index)

def bfs(root, node_to_index):
    queue = deque([(root, 1)])
    level_min_max = {}
    while queue:
        node, level = queue.popleft()
        index = node_to_index[node.number]
        if level in level_min_max:
            level_min_max[level] = (min(level_min_max[level][0], index), max(level_min_max[level][1], index))
        else:
            level_min_max[level] = (index, index)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return level_min_max

n = int(input())  # Number of nodes
nodes = {i: Node(i) for i in range(1, n + 1)}
not_root = set()  # 루트가 될 수 없는 노드의 집합

for _ in range(n):
    number, left, right = map(int, input().split())
    if left != -1:
        nodes[number].left = nodes[left]
        not_root.add(left)
    if right != -1:
        nodes[number].right = nodes[right]
        not_root.add(right)

root_number = (set(nodes.keys()) - not_root).pop()  # 집합 연산을 통해 루트 노드 번호를 찾음
root = nodes[root_number]

# In-order traversal to get column order and node-to-index mapping
column_order = []
node_to_index = {}
in_order_traversal(root, column_order, node_to_index)

# BFS to calculate width of each level
level_min_max = bfs(root, node_to_index)

# Find the level with the maximum width
max_width = 0
max_level = 0
for level, (min_index, max_index) in level_min_max.items():
    width = max_index - min_index + 1
    if width > max_width:
        max_width = width
        max_level = level

print(max_level, max_width)