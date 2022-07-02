class Leaf:
	def __init__(self, val = None):
		self.next = None
		self._data = val

	@property
	def data(self):
		return self._data

	def enqueue(self, new_data):
		if self.next:
			self.next.enqueue(new_data)
		else:
			self.next = Leaf(new_data)

	def all_data(self) -> []:
		cursor = self
		alldata = [self.data]
		while cursor.next:
			cursor = cursor.next
			alldata.append(self.data)
		return alldata

	# Overloading  == , > , str operators
	def __eq__(self, other):
		return self.data == other

	def __gt__(self, other):
		if self.data > other:
			return True
		else:
			return False

	def __str__(self):
		return str(self.all_data())

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
		self.leaf = node
		self.left = None
		self.right = None

	def insert(self, new_node):
		if not self.leaf:
			self.leaf = Leaf(new_node)
			return

		if self.leaf == new_node:
			self.leaf.enqueue(new_node)
			return

		if new_node < self.leaf:
			if self.left:
				self.left.insert(new_node)
				return
			self.left = BinarySearchTree(Leaf(new_node))
			return
		elif self.right:
			self.right.insert(new_node)
			return
		self.right = BinarySearchTree(Leaf(new_node))

	def print_inorder(self):
		if self.left:
			self.left.print_inorder()
		if self.leaf:
			print(self.leaf, end = " ")
		if self.right is not None:
			self.right.print_inorder()
