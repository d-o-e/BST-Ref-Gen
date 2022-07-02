class Node:
	def __init__(self, val = None):
		self.queue = 0
		# TODO: 7/2/22 change it to a queue and to a simple list after
		self.word = val

	@property
	def get_word(self):
		return self.word

	def increment_queue(self):
		self.queue += 1

	# Overloading  == , > , str operators
	def __eq__(self, other):
		return self.word == other.word

	def __gt__(self, other):
		if self.word > other.word:
			return True
		else:
			return False

	def __str__(self):
		return str(self.word)


class BinarySearchTree:
	def __init__(self, node = None):
		self.leaf = node
		self.left = None
		self.right = None

	def insert(self, new_node):
		if not self.leaf:
			self.leaf = new_node
			return

		if self.leaf == new_node:
			self.leaf.increment_queue()
			return

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

	# will add delete function

	def print_inorder(self):
		if self.left:
			self.left.print_inorder()
		if self.leaf:
			print(self.leaf, end = " ")
		if self.right is not None:
			self.right.print_inorder()


class Queue:
	def __init__(self, node = None):
		self.val = node
		self.next = None

	@property
	def get_value(self):
		return self.val

	def enqueue(self, node):
		if self.next:
			self.next.enqueue(node)
		else:
			self.val = node

	def dequeue(self) -> Node:
		if self.next:
			self.dequeue()
		else:
			return self.val

	class QNode:
		def __init__(self, data = None):
			self.data = data


