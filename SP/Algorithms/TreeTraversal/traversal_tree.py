class TreeNode:

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)


def create_sample_tree():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(7)

    return root


if __name__ == "__main__":
    inorder_traversal(create_sample_tree())