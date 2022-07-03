import errno
import re
from sys import stderr as error


split_delimiters = r'[\s,.?\"\-!\n\t]'


class DataReader:
    """Data reader class"""


    def __init__(self, filename = None):
        self._words = {}
        try:
            with open(filename, "r") as file_out:
                line_number = 1
                for line in file_out:
                    temp_words = filter(lambda word: word, re.split(
                        split_delimiters, line.strip()))
                    if temp_words:
                        self._words[line_number] = list(temp_words)
                    line_number += 1
        except FileExistsError:
            print(f"{errno.ENOENT}: File not found", file = error)


    @property
    def words(self):
        return self._words
