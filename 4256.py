# https://www.acmicpc.net/problem/4256

# tree
# A binary tree is a basic and important data structure. As illustrated in Figure 1, a binary tree has a unique root node. Each node has at most two child nodes that are ordered from left to right. Let BT be a binary tree of n nodes. Nodes of BT have unique id numbers from 1 to n. 

# For BT in Figure 1, the node of id 3 is the root node. The node of id 1 has only right child node, but two nodes of id 4 and id 7 have only left child nodes. Two nodes of id 3 and id 6 have left and right child nodes. The other nodes, called leaf nodes, have no child nodes. 



# Figure 1. A binary tree with 8 nodes. The dashed vertical lines from the nodes are imaginary lines to distinguish their left and right child nodes 

# We have three methods to traverse all nodes of BT; preorder, inorder, and postorder traversals. These three traversals are done by the following C-style pseudo codes: For a node v of BT, we denote by v.left and v.right its left child node and right child node, respectively. If v has no left child, then v.left is equal to ∅. If v has no right child, then v.right is equal to ∅. 



# You are now given two lists of id numbers of BT; one is the list obtained by preorder traversal and the other is by inorder traversal, i.e., two lists obtained by calling preorder(root node of BT) and inorder(root node of BT). It is well known that BT can be reconstructed from these two lists. You need to reconstruct BT from the preorder and inorder traversal lists of BT, and output its postorder traversal list which should be the same as the result of postorder(root node of BT). 

# For example, if you are given preorder traversal list of 3, 6, 5, 4, 8, 7, 1, 2 and inorder traversal list of 5, 6, 8, 4, 3, 1, 2, 7, then you should reconstruct the tree as in Figure 1, and output its postorder traversal list, which is 5, 8, 4, 6, 2, 1, 7, 3. 

# input
# Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with integer n, the number of nodes of a rooted and ordered binary tree BT, where 1 ≤ n ≤ 1,000. Nodes of BT are assumed to have distinct id number from 1 to n. The next line contains a list of n numbers, i.e., a permutation of {1,2, ⋯ , n}, which is the preorder traversal list of BT. The next line contains a list of n numbers, i.e., a permutation of {1,2, ⋯ , n}, which is the inorder traversal list of the same BT. Two neighboring node id numbers in these lists have a single space between them. Note that a unique binary tree is always constructed from these preorder and inorder traversal lists. 

# output
# Your program is to write to standard output. Print exactly one line for each test case. The line should contain a permutation of n numbers of {1,2, ⋯ , n}, which is the same as the postorder traversal list of BT. 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

def postorderTraversal(root):
    res = []
    if root:
        res = postorderTraversal(root.left)
        res += postorderTraversal(root.right)
        res.append(root.val)
    return res

def reconstruct_and_postorder():
    T = int(input())  # Number of test cases
    for _ in range(T):
        n = int(input())  # Number of nodes
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))

        # Reconstruct the tree and perform postorder traversal
        tree = buildTree(preorder, inorder)
        postorder = postorderTraversal(tree)
        print(' '.join(map(str, postorder)))

# Call the function to process input and generate output
reconstruct_and_postorder()