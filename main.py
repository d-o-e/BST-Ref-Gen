import random

from BST import BinarySearchTree as Bst
from BST import Node as Node


def main():
	my_tree = Bst()
	nums = [12, 6, 18, 19, 21, 11, 6, 3, 5, 4, 24, 18]
	nums.extend([random.randint(0, 400) for x in range(100)])
	for num in nums:
		my_tree.insert(Node(num))

	my_tree.printInorder()


if __name__ == '__main__':
	main()
