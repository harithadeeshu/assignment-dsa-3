class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return max(left_height, right_height) + 1

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node is not None:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")

    def print_leaves(self):
        self._print_leaves_recursive(self.root)

    def _print_leaves_recursive(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self._print_leaves_recursive(node.left)
            self._print_leaves_recursive(node.right)

    def bfs(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        self._dfs_recursive(self.root)

    def _dfs_recursive(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._dfs_recursive(node.left)
            self._dfs_recursive(node.right)

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, node, is_left):
        if node is None:
            return 0
        if node.left is None and node.right is None and is_left:
            return node.data
        return (
            self._sum_left_leaves_recursive(node.left, True)
            + self._sum_left_leaves_recursive(node.right, False)
        )

    def sum_all_nodes(self):
        return self._sum_all_nodes_recursive(self.root)

    def _sum_all_nodes_recursive(self, node):
        if node is None:
            return 0
        return (
            node.data
            + self._sum_all_nodes_recursive(node.left)
            + self._sum_all_nodes_recursive(node.right)
        )

    def count_subtrees_with_sum(self, x):
        count = [0]
        self._count_subtrees_with_sum_recursive(self.root, x, count)
        return count[0]

    def _count_subtrees_with_sum_recursive(self, node, x, count):
        if node is None:
            return 0
        left_sum = self._count_subtrees_with_sum_recursive(node.left, x, count)
        right_sum = self._count_subtrees_with_sum_recursive(node.right, x, count)
        current_sum = node.data + left_sum + right_sum
        if current_sum == x:
            count[0] += 1
        return current_sum

    def max_level_sum(self):
        if self.root is None:
            return 0
        queue = [self.root]
        max_sum = float('-inf')
        while queue:
            level_sum = sum(node.data for node in queue)
            max_sum = max(max_sum, level_sum)
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        return max_sum

    def print_odd_level_nodes(self):
        self._print_odd_level_nodes_recursive(self.root, 1)

    def _print_odd_level_nodes_recursive(self, node, level):
        if node is None:
            return
        if level % 2 == 1:
            print(node.data, end=" ")
        self._print_odd_level_nodes_recursive(node.left, level + 1)
        self._print_odd_level_nodes_recursive(node.right, level + 1)
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print("Height of the tree:", tree.height())

print("Pre-order traversal:")
tree.preorder_traversal()
print()

print("Post-order traversal:")
tree.postorder_traversal()
print()

print("In-order traversal:")
tree.inorder_traversal()
print()

print("Leaves in the tree:")
tree.print_leaves()
print()

print("BFS traversal:")
tree.bfs()
print()

print("DFS traversal:")
tree.dfs()
print()

print("Sum of all left leaves:", tree.sum_left_leaves())

print("Sum of all nodes in the tree:", tree.sum_all_nodes())

x = 22
print("Number of subtrees with sum", x, ":", tree.count_subtrees_with_sum(x))

print("Maximum level sum:", tree.max_level_sum())

print("Nodes at odd levels:")
tree.print_odd_level_nodes()
