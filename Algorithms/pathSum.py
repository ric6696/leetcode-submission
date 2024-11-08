import sys

from TreeNode import list_to_binary_tree, print_tree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right and targetSum == root.val:
        return True

    targetSum = targetSum - root.val

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


def main():
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    root = list_to_binary_tree(root)
    print(hasPathSum(root, targetSum))


if __name__ == "__main__":
    sys.exit(main())
