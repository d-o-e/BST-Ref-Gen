from threading import Thread
from time import sleep

from BST import BinarySearchTree as Bst
from BST import Leaf
from DataReader import DataReader as Reader


def reading():
	for i in range(100):
		sleep(0.1)
		print("thread running")


def main():
	my_tree = Bst()
	# nums = []
	# nums.extend([rand(0, 100) for x in range(200)])
	# for num in nums: my_tree.insert(num)
	reader = Reader("speech.txt")
	for val in reader.words.keys():
		for word in reader.words[val]:
			my_tree.insert(Leaf((val, word)))
	del reader, word, val
	my_tree.print_inorder()
	# del my_tree

	my_tree.search("of")



if __name__ == '__main__':
	# trying threading
	main_thread = Thread(target = main)
	read_thread = Thread(target = reading)
	read_thread.start()
	sleep(1)
	main_thread.start()