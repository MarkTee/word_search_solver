#!/usr/bin/env python3
from trie import Trie, TrieNode

class WordSearch:

    def __init__(self, rows, columns, grid, word_list):
        self._rows = rows
        self._columns = columns
        self._grid = grid
        self._word_list = word_list
        self._trie = Trie()

    def build_trie(self):
        for word in self._word_list:
            self._trie.insert_word(word)

    def print_grid(self):
        print()
        for row in self._grid:
            print(' '.join(row))

    def print_word_list(self):
        print()
        for word in self._word_list:
            print(word)

    def find_horizontal_matches(self):
        for row in self._grid:
            pass

# Helper functions to build a WordSearch object from input files

def format_grid(filename):
    """Scrape a text file and convert it into a 2d list, representing the word search's grid."""
    grid = []

    # Scrape the file line-by-line (row-by-row), and place the letters in a list
    input_file = open(filename, 'r')
    for line in input_file.read().splitlines():
        line = line.replace(' ', '')
        row = list(line)
        grid.append(row)
    input_file.close()

    return grid

def format_word_list(filename):
    input_file = open(filename, 'r')
    word_list = input_file.read()
    input_file.close()

    # Extract words from a comma-separated list
    word_list = word_list.split(',')

    # Remove leading and trailing spaces from all words
    word_list = [word.strip(' ') for word in word_list]

    return word_list

def create_word_search(grid, word_list):
    grid_height = len(grid)
    grid_width = len(grid[0])

    return WordSearch(grid_height, grid_width, grid, word_list)

def main():
    grid = format_grid('sample_grid.txt')
    word_list = format_word_list('sample_word_list.txt')
    word_search = create_word_search(grid, word_list)
    word_search.build_trie()
    word_search.print_grid()
    word_search.print_word_list()

if __name__ == '__main__':
    main()
