# Deniz Erisgen ©
from sys import stderr as error


class Leaf:
    def __init__(self, val = None):
        if val is not None:
            self.lines = [val[0]]
            self._data = val[1]
        else:
            self._data = None


    @property
    def data(self):
        return self._data


    def add_line_number(self, leaf) -> bool:
        if leaf is not None and leaf.lines is not None:
            self.lines.append(leaf.lines[0])
            return True
        else:
            return False

    # Overloading  == , > , str operators below

    def __eq__(self, other):
        return self.data == other.data


    def __gt__(self, other):
        if self.data > other.data:
            return True
        else:
            return False


    def __str__(self):
        if self.data:
            return str(self.data + ": " + str(self.lines) + '\n')
        else:
            return ''


# Different all data print option
# def __str__(self):
# 	cursor = self
# 	whole = "Leaf Node: (" + str(cursor.data)
# 	while cursor.next:
# 		whole += ', ' + str(cursor.data)
# 		cursor = cursor.next
# 	whole += ')'
# 	return str(whole)


class BinarySearchTree:
    def __init__(self, node = None):
        if node is not None:
            self.leaf = node
            self.left = None
            self.right = None
        else:
            self.leaf = None


    def insert(self, new_node):
        """
        Inserts data to the tree
        :param new_node: Data to store
        :return:
        """
        if new_node is None:
            print("Node is not defined", file = error)
            return

        if not self.leaf:
            self.leaf = new_node
            return

        if self.leaf == new_node:
            if self.leaf.add_line_number(new_node):
                return
            else:
                print("Can't insert")

        if new_node < self.leaf:
            if self.left:
                self.left.insert(new_node)
                return
            self.left = BinarySearchTree(new_node)
            return
        elif self.right:
            self.right.insert(new_node)
            return
        self.right = BinarySearchTree(new_node)


    def print_inorder(self):
        """
        Prints the tree depth first order
        """
        if self.left:
            self.left.print_inorder()
        if self.leaf:
            print(self.leaf, end = " ")
        if self.right is not None:
            self.right.print_inorder()


    def search(self, term):
        if term is None: return
        cursor = self
        if term == cursor.leaf.data:
            print(cursor.leaf)
        elif term < cursor.leaf.data and cursor.left:
            cursor = cursor.left
            cursor.search(term)
        elif term > cursor.leaf.data and cursor.right:
            cursor = cursor.right
            cursor.search(term)
        else:
            print("Not found")
