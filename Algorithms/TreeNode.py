class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(data_list):
    if not data_list:
        return None

    root = TreeNode(data_list[0])
    queue = [root]
    index = 1

    while index < len(data_list):
        current = queue.pop(0)

        if index < len(data_list) and data_list[index] is not None:
            current.left = TreeNode(data_list[index])
            queue.append(current.left)
        index += 1

        if index < len(data_list) and data_list[index] is not None:
            current.right = TreeNode(data_list[index])
            queue.append(current.right)
        index += 1

    return root


def print_tree(root):
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
    return
