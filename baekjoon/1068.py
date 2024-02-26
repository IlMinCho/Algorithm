# https://www.acmicpc.net/problem/1068

# 트리

# 문제
# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

# 예를 들어, 다음과 같은 트리가 있다고 하자.



# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.



# 이제 리프 노드의 개수는 1개이다.

# 입력
# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

def dfs(tree, node):
    tree[node] = -2  # 노드 삭제 표시
    for i in range(len(tree)):
        if tree[i] == node:  # 삭제된 노드를 부모로 가지는 노드 찾기
            dfs(tree, i)  # 재귀적으로 삭제

def count_leaf_nodes(tree):
    count = 0
    for i in range(len(tree)):
        if tree[i] != -2 and i not in tree:  # 삭제되지 않았고, 다른 노드의 부모도 아닌 경우
            count += 1
    return count

def main():
    N = int(input())
    tree = list(map(int, input().split()))
    remove_node = int(input())

    dfs(tree, remove_node)  # 삭제할 노드와 자손 노드들 제거
    leaf_count = count_leaf_nodes(tree)  # 리프 노드의 개수 계산
    print(leaf_count)

if __name__ == "__main__":
    main()