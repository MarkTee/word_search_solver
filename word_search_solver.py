#!/usr/bin/env python3
from trie import Trie


class WordSearch:

    def __init__(self, grid, word_list):
        self.grid = grid
        self.word_list = word_list
        self.remaining_words = set(word_list)
        self.found_words = []
        self.trie = Trie()

    def build_trie(self):
        for word in self.word_list:
            self.trie.insert_word(word)

    def print_grid(self):
        print()
        for row in self.grid:
            print(' '.join(row))

    def print_word_list(self):
        print()
        for word in self.word_list:
            print(word)

    def get_letter(self, row, column):
        return self.grid[row][column]

    # def find_words(self):
    #     row_index = 0
    #     for row in self.grid:
    #         col_index = 0
    #         for letter in row:
    #             self.check_adjacent_tiles(letter, row_index, col_index)
    #             col_index += 1
    #         row_index += 1

    # def check_adjacent_tiles(self, prefix, row_index, col_index):
    #     if prefix in self.word_list_set:
    #         self.found_words.append(prefix)
    #         self.word_list_set.remove(prefix)
    #         # print(self.word_list_set)
    #         prefix = prefix[0]
    #         return True

    #     if self.trie.contains_prefix(prefix):
    #         # Check horizontal matches
    #         if col_index + 1 <= self._columns:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index, col_index+1), row_index, col_index+1)

    #         if col_index - 1 >= 0:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index, col_index-1), row_index, col_index-1)

    #         # Check vertical matches
    #         if row_index + 1 <= self._rows:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index), row_index+1, col_index)

    #         if row_index - 1 <= 0:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index), row_index-1, col_index)

    #         # Check diagonal matches
    #         if row_index - 1 >= 0 and col_index + 1 <= self._columns:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index+1), row_index-1, col_index+1)

    #         if row_index + 1 <= self._rows and col_index + 1 <= self._columns:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index+1), row_index+1, col_index+1)

    #         if row_index - 1 >= 0 and col_index - 1 >= 0:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index-1, col_index-1), row_index-1, col_index-1)

    #         if row_index + 1 <= self._rows and col_index + 1 >= 0:
    #             self.check_adjacent_tiles(prefix+self.get_letter(row_index+1, col_index-1), row_index+1, col_index-1)

    #     return False

    def solve(self):
        while self.remaining_words:
            row_index = 0
            for row in self.grid:
                col_index = 0
                for letter in row:
                    # If the cell contains a letter that is the first letter of one of the words
                    if self.trie.contains_prefix(letter):
                        self.traverse_tiles(letter, row_index, col_index)
                    col_index += 1
                row_index += 1

    def traverse_tiles(self, letter, row_index, col_index):
        # if prefix in self.remaining_words:
        #     self.found_words.append(prefix)
        #     self.remaining_words.remove(prefix)
        directions = {'right': (0, 1),
                    'down-right': (1, 1),
                    'down': (1, 0),
                    'down-left': (1, -1),
                    'left': (0, -1),
                    'up-left': (-1, -1),
                    'up': (-1, 0),
                    'up-right': (-1, 1)}

        for direction_name in directions:
            direction = directions[direction_name]
            prefix = letter
            next_row_index = row_index
            next_col_index = col_index
            i = 1

            while True:
                next_row_index += direction[0]
                next_col_index += direction[1]
                try:
                    prefix += self.get_letter(next_row_index, next_col_index)
                except IndexError:
                    break

                if self.trie.contains_prefix(prefix):
                    if prefix in self.remaining_words:
                        self.found_words.append(prefix)
                        self.remaining_words.remove(prefix)
                        print("'{}' can be found at row {}, column {} and moving {}".format(prefix, row_index, col_index, direction_name))
                        break
                    else:
                        continue
                else:
                    break

            if len(self.remaining_words) == 0:
                print("solved!")
                exit()


            # self.traverse_adjacent_tiles(prefix, row_index, col_index, directions[direction])

    # def traverse_adjacent_tiles(self, prefix, row_index, col_index, direction):
    #     prefix += self.get_letter(row_index, col_index)

    # def check_adjacent_tiles(self, prefix, row_index, col_index):
    #     if self.trie.contains_prefix(prefix):
    #         return -1


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



def main():
    grid = build_grid('sample_grid.txt')
    word_list = build_word_list('sample_word_list.txt')
    word_search = WordSearch(grid, word_list)
    word_search.build_trie()
    word_search.solve()
    # word_search.find_words()
    # word_search.print_grid()
    # word_search.print_word_list()

if __name__ == '__main__':
    main()
