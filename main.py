from BST import BinarySearchTree as BST
from BST import Node as Node


def main():
	mytree = BST()
	nums = [12, 6, 18, 19, 21, 11, 6, 3, 5, 4, 24, 18]
	for num in nums:
		mytree.insert(Node(num))

	mytree.printInorder()


if __name__ == '__main__':
	main()
