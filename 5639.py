# https://www.acmicpc.net/problem/5639

# 이진 검색트리
# 문제
# 이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진 트리이다.

# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.


# 전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

# 입력
# 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

# 출력
# 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.


외부 입력을 받아 처리하는 프로그램을 만들기 위해서는 사용자로부터 입력을 받는 방법을 포함해야 합니다. Python에서는 input() 함수를 사용하여 사용자의 입력을 받을 수 있습니다. 그러나 이 환경에서는 실시간 사용자 입력을 받는 것이 불가능합니다. 대신, 외부 입력을 받는 코드 예제를 제공할 수 있으며, 이 코드는 로컬 환경이나 다른 Python 실행 환경에서 실행해 볼 수 있습니다.

아래는 외부에서 전위 순회 결과를 입력으로 받아 이진 검색 트리를 후위 순회로 출력하는 전체 Python 프로그램의 예제입니다. 이 코드는 표준 입력으로부터 여러 줄에 걸쳐 전위 순회 결과를 받아들이고, 입력이 끝나면 후위 순회 결과를 출력합니다. 입력 종료는 파일 끝(EOF)으로 표시됩니다. Linux나 macOS에서는 Ctrl+D를, Windows에서는 Ctrl+Z를 사용하여 EOF를 입력할 수 있습니다.

python
Copy code
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def postOrderTraversal(root, result=[]):
    if root:
        postOrderTraversal(root.left, result)
        postOrderTraversal(root.right, result)
        result.append(root.data)
    return result

def main():
    root = None
    try:
        while True:
            data = int(input())  # 전위 순회 결과로부터 노드 값 하나씩 입력 받음
            root = insert(root, data)
    except EOFError:
        pass  # 입력 종료

    # 후위 순회 결과 출력
    postOrderResult = postOrderTraversal(root, [])
    for data in postOrderResult:
        print(data)

if __name__ == "__main__":
    main()