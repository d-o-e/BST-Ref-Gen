import errno
import re

split_delimiters = r'[\s,.?\"\-!\n\t]'


class DataReader:
	"""Data reader class"""
	def __init__(self, filename = None):
		self._words = {}
		try:
			with open(filename, "r") as fout:
				line_number = 1
				for line in fout:
					temp_words = list(filter(lambda word: word, re.split(split_delimiters, line.strip())))
					if temp_words: self._words[line_number] = temp_words
					line_number += 1
		except FileExistsError:
			print(f"{errno.ENOENT}: File not found")

	@property
	def words(self):
		return self._words
