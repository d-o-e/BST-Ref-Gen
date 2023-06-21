# Deniz Erisgen ©
from threading import Thread

from bst import BinarySearchTree as Bst, Leaf
from datareader import DataReader as Reader

my_tree = Bst()
filename = 'speech.txt'


def read_file():
    global my_tree, filename
    reader = Reader(filename)
    for val in reader.words():
        for word in val:
            my_tree.insert(Leaf((val, word)))
    del reader, word, val


def print_tree():
    global my_tree
    my_tree.print_inorder()


def main():
    print_tread = Thread(target=print_tree)
    read_thread = Thread(target=read_file)
    read_thread.start()
    read_thread.join()  # remove join and break the program
    print_tread.start()


if __name__ == '__main__':
    # trying threading
    main()