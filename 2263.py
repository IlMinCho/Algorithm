# https://www.acmicpc.net/problem/2263

# 트리의 순회
# 문제
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

# 출력
# 첫째 줄에 프리오더를 출력한다.
def construct_preorder(inorder, postorder, in_start, in_end, post_start, post_end, in_map):
    if (in_start > in_end) or (post_start > post_end):
        return []
    
    root = postorder[post_end]
    in_root_index = in_map[root]
    left_subtree_length = in_root_index - in_start
    
    preorder = [root] + \
               construct_preorder(inorder, postorder, in_start, in_root_index-1, post_start, post_start+left_subtree_length-1, in_map) + \
               construct_preorder(inorder, postorder, in_root_index+1, in_end, post_start+left_subtree_length, post_end-1, in_map)
    return preorder

def find_preorder(inorder, postorder):
    in_map = {value: idx for idx, value in enumerate(inorder)}
    return construct_preorder(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1, in_map)

# 트리의 크기를 입력받습니다.
n = int(input())

# 인오더 리스트를 입력받습니다.
inorder = list(map(int, input().split()))

# 포스트오더 리스트를 입력받습니다.
postorder = list(map(int, input().split()))

# 프리오더를 계산하여 출력합니다.
preorder = find_preorder(inorder, postorder)
print(" ".join(map(str, preorder)))