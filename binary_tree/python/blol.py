

def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    left_subtree = root.pop(1)
    if len(left_subtree) > 1:  # if there are nodes in left subtree
        # the new branch becomes the left node and the existing one
        # is the first left children of the new branch
        root.insert(1, [new_branch, left_subtree, []])
    else:
        root.insert(1, [new_branch, [], []])


def insert_right(root, new_branch):
    right_subtree = root.pop(2)
    if len(right_subtree) > 1:
        root.insert(2, [new_branch, [], right_subtree])
    else:
        root.insert(2, [new_branch, [], []])


def get_root_val(root):
    # should be a list
    return root[0]


def set_root_val(root, new_root):
    # root and new_root should be list
    root[0] = new_root


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def build_example_tree():
    r = binary_tree('a')
    insert_left(r, 'b')
    insert_right(get_left_child(r), 'd')
    insert_right(r, 'c')
    insert_left(get_right_child(r), 'e')
    insert_right(get_right_child(r), 'f')
    return r
