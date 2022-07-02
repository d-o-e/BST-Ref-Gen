from BST import BinarySearchTree as Bst
from random import randint as rand


def main():
	my_tree = Bst()
	nums = []
	nums.extend([rand(0, 100) for x in range(200)])
	for num in nums: my_tree.insert(num)

	my_tree.print_inorder()
	del my_tree


if __name__ == '__main__':
	main()
