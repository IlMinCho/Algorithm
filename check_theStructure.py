# To solve the provided problem, let's implement a function that verifies if a given pre-order traversal 
# list of a binary tree represents a valid binary search tree (BST).
# The algorithm will maintain a stack to keep track of the nodes and their valid value ranges.

def is_valid_BST(preorder):
    stack = []
    lower_bound = float('-inf')

    for value in preorder:
        if value < lower_bound:
            return 'NO'
        while stack and value > stack[-1]:
            lower_bound = stack.pop()
        stack.append(value)

    return 'YES'