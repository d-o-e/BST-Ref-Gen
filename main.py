from BST import BinarySearchTree as Bst
from random import randint as rand


def main():
	my_tree = Bst()
	nums = []
	nums.extend([rand(0, 20) for x in range(100)])
	for num in nums: my_tree.insert(num)

	my_tree.print_inorder()


if __name__ == '__main__':
	main()
