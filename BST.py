class Node:
	def __init__(self, val = None):
		self.val = val

	@property
	def node(self):
		return self.val

	"""
		@node.setter
		def node(self, value):
			self.val = value
	"""

	# Overloading  == , > , str operators
	def __eq__(self, other):
		return self.val == other.val

	def __gt__(self, other):
		if self.val > other.val:
			return True
		else:
			return False

	def __str__(self):
		return str(self.val)


class BinarySearchTree:
	def __init__(self, node = None):
		self.left = None
		self.right = None
		self.node = node  # will be changed to a queue

	def insert(self, new_node):
		if not self.node:
			self.node = new_node
			return

		if self.node == new_node:
			print(f"{self.node} and {new_node} equal vals ")
			# insert to the queue
			return

		if new_node < self.node:
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

	def printInorder(self):
		if self.left is not None:
			self.left.printInorder()
		if self.node is not None:
			print(self.node, end = " ")
		if self.right is not None:
			self.right.printInorder()
