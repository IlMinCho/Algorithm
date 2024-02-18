# https://www.acmicpc.net/problem/9489

# 사촌
# 문제
# 증가하는 정수 수열을 이용해서 트리를 만드는 방법은 다음과 같다.

# 첫 번째 정수는 트리의 루트 노드이다.
# 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타낸다. 이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1보다 크다.
# 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 된다. 그러한 노드가 여러 가지 인 경우에는 가장 작은 수를 가지는 노드의 자식이 된다.
# 집합은 수가 연속하지 않는 곳에서 구분된다.
# 예를 들어, 수열 1 3 4 5 8 9 15 30 31 32를 위의 규칙을 이용해 트리를 만들면 아래 그림과 같이 된다.



# 두 노드의 부모는 다르지만, 두 부모가 형제(sibling)일 때 두 노드를 사촌이라고 한다.

# 수열 특정 노드 번호 k가 주어졌을 때, k의 사촌의 수를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 노드의 수 n과 사촌의 수를 구해야 하는 노드의 번호 k가 주어진다. (1 ≤ n ≤ 1,000, 1 ≤ k ≤ 1,000,000) 다음 줄에는 총 n개의 수가 주어지며, 모든 수는 1보다 크거나 같고, 1,000,000보다 작거나 같다. 입력으로 주어지는 수열은 항상 증가한다. k는 항상 수열에 포함되는 수이다.

# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각 테스트 케이스 마다, k의 사촌의 수를 출력한다.

# 다시 분석하고 문제를 해결하기 위한 코드를 작성합니다.

import sys

def find_cousins():
    while 1:
        n, k = map(int, sys.stdin.readline().split())
        if n == 0 and k == 0:
            break
        else:
            dic = {}
            n_list = list(map(int, sys.stdin.readline().split()))
            cnt = 0

            parent = []
            if len(n_list) > 1:
                next = n_list[1]
            parent.append(next)
            for i in range(2, n):
                if (n_list[i] - 1) == next:
                    parent.append(n_list[i])
                    next = n_list[i]

                else:
                    dic[n_list[cnt]] = parent
                    parent = []
                    parent.append(n_list[i])
                    next = n_list[i]
                    cnt += 1
                if i == n - 1:
                    dic[n_list[cnt]] = parent

            # 부모 노드 찾기
            for i in dic.keys():
                if k in dic[i]:
                    root = i
                    break
            found = 0

            # 조부모 노드 찾기
            for i in dic.keys():
                if root in dic[i]:
                    par = i
                    found = 1
                    break
            if found == 0:
                print(0)
            else:
                ans = 0
                # 사촌 수 계산
                for i in dic[par]:
                    if i != root and (i in dic):
                        ans += len(dic[i])
                print(ans)

if __name__ == "__main__":
    find_cousins()


