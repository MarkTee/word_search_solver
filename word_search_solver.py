#!/usr/bin/env python3
from trie import Trie


class WordSearch:

    def __init__(self, grid, word_list):
        self._grid = grid
        self._word_list = word_list
        self._word_list_set = set(word_list)
        self._found_words = []
        self._solutions = []
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

    def get_letter(self, row, column):
        return self._grid[row][column]

    # def find_words(self):
    #     row_index = 0
    #     for row in self._grid:
    #         col_index = 0
    #         for letter in row:
    #             self.check_adjacent_tiles(letter, row_index, col_index)
    #             col_index += 1
    #         row_index += 1

    # def check_adjacent_tiles(self, prefix, row_index, col_index):
        if prefix in self._word_list_set:
            self._found_words.append(prefix)
            self._word_list_set.remove(prefix)
            # print(self._word_list_set)
            prefix = prefix[0]
            return True

        if self._trie.find_prefix(prefix):
            # Check horizontal matches
            if col_index + 1 <= self._columns:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index, col_index+1), row_index, col_index+1)

            if col_index - 1 >= 0:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index, col_index-1), row_index, col_index-1)

            # Check vertical matches
            if row_index + 1 <= self._rows:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index), row_index+1, col_index)

            if row_index - 1 <= 0:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index), row_index-1, col_index)

            # Check diagonal matches
            if row_index - 1 >= 0 and col_index + 1 <= self._columns:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index+1), row_index-1, col_index+1)

            if row_index + 1 <= self._rows and col_index + 1 <= self._columns:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index+1), row_index+1, col_index+1)

            if row_index - 1 >= 0 and col_index - 1 >= 0:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index-1), row_index-1, col_index-1)

            if row_index + 1 <= self._rows and col_index + 1 >= 0:
                self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index-1), row_index+1, col_index-1)

        return False

    def solve(self):
        row_index = 0
        for row in self._grid:
            col_index = 0
            for col in row:
                self.check_adjacent_tiles(cell, row_index, col_index)
                col_index += 1
            row_index += 1

    def check_adjacent_tiles(self, prefix, row_index, col_index):
        if self._trie.find_prefix(prefix):
            return -1


# Helper functions to build a WordSearch object from input files

def build_grid(filename):
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

def build_word_list(filename):
    input_file = open(filename, 'r')
    word_list = input_file.read()
    input_file.close()

    # Extract words from a comma-separated list
    word_list = word_list.split(',')

    # Remove leading and trailing spaces from all words
    word_list = [word.strip(' \n') for word in word_list]

    return word_list

def build_word_search(grid, word_list):
    grid_height = len(grid)
    grid_width = len(grid[0])

    return WordSearch(grid_height, grid_width, grid, word_list)



def main():
    grid = build_grid('sample_grid.txt')
    word_list = build_word_list('sample_word_list.txt')
    word_search = build_word_search(grid, word_list)
    word_search.build_trie()
    word_search.solve()
    # word_search.print_grid()
    # word_search.print_word_list()

if __name__ == '__main__':
    main()
