from BST import BinarySearchTree as Bst
from BST import Node as Node
from random import randint as rand


def main():
	my_tree = Bst()
	nums = []
	nums.extend([rand(0, 500) for x in range(100)])
	for num in nums:
		my_tree.insert(Node(num))

	my_tree.print_inorder()


if __name__ == '__main__':
	main()
