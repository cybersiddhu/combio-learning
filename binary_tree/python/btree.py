class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        """insert node in tree"""
        if self.root:
            self.insert_node(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def insert_node(self, key, value, current_node):
        """insert a node in the tree, internal method"""
        """if the given value is less than the current node, recursively """
        """search the left tree. For each node pick up the left child unless"""
        """you hit the leaf. In case the value is higher drill"""
        """down through the right tree"""
        if key < current_node.key:
            if current_node.has_left_child():
                self.insert_node(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key,
                                                   value, parent=current_node)
        else:
            if current_node.has_right_child():
                self.insert_node(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key,
                                                    value, parent=current_node)

    def get(self, key):
        """retrieve a node"""
        if self.root:
            node = self.retrieve_node(key, self.root)
            if node:
                return node.payload
            else:
                return None
        else:
            return None

    def retrieve_node(self, key, current_node):
        """retrieve a node, internal method"""
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            self.retrieve_node(key, current_node.left_child)
        else:
            self.retrieve_node(key, current_node.right_child)

    def delete(self, key):
        """Removing a node. Retrieve the node to remove it"""
        if self.size > 1:
            node = self.retrieve_node(key, self.root)
            if node:
                self.remove_node(node)
                self.size = self.size - 1
            else:
                raise KeyError("Error key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error key not in tree")

    def remove_node(self, node):
        """Remove a node, internal method"""
        # First case is leaf node
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        # Second case node with both children
        elif node.has_both_children():
            # In this case the selected successor has to maintain the property
            # of binary tree. This means we leave out left subtree as
            # the keys of the nodes are already less than their parent.
            # So, we follow the right subtree.
            # By default, any children of the right branch will always
            # have greater key than the
            # current node to be removed. So, this will preseve the left side
            # property of the binary tree. Now, for the right side we need to
            # get a successor in that right subtree with the smallest key.
            # So, we drill down through the left subtree.
            # 1. We get the successor
            succ = node.find_successor()
            # 2. Yank the successor node preserving the binary tree
            succ.splice_out()
            node.key = succ.key
            node.payload = succ.payload
        # Last case node with a child
        else:
            if node.has_left_child():
                if node.is_left_child():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:  # node is root
                    left_child = node.left_child
                    node.replace_node_data(left_child.key, left_child.payload,
                                           left_child.left_child,
                                           left_child.right_child)
            else:
                if node.is_left_child():
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:  # node is root
                    right_child = node.right_child
                    node.replace_node_data(right_child.key,
                                           right_child.payload,
                                           right_child.left_child,
                                           right_child.right_child)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.retrieve_node(key, self.root):
            return True
        else:
            return False


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.parent = parent
        self.left_child = left
        self.right_child = right

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child and self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self

        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        succ = None
        # if the node has a right child, then the successor
        # is the smallest key in the right subtree
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            # just do not understand this whole section
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        # walks down the left subtree unless find a node without a left child
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        # first case there will be no left or right child pointer
        # for the parent
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # in this case depending on left or right child we
        # reset the pointer both
        # for parent and left/right child
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
