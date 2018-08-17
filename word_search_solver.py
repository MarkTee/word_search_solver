#!/usr/bin/env python3
from trie import Trie


class WordSearch:
    """Contains all relevant information for a particular word search,
    including:

    - Puzzle grid
    - Word list (and it's corresponding trie)
    - Methods to display and solve the word search
    """

    def __init__(self, grid, word_list):
        """Inits a WordSearch object.

        - Separates the word list into those that have been found and those
        that remain hidden.

        - Builds a trie representing the WordSearch's words.
        """
        self.grid = grid
        self.word_list = word_list
        self.remaining_words = set(word_list)
        self.found_words = []

        self.trie = Trie()
        self.build_trie()

    def build_trie(self):
        """Populate the trie with all words from the word list."""
        for word in self.word_list:
            self.trie.insert_word(word)

    def print_grid(self):
        """Print the word search grid to the terminal."""
        print()
        for row in self.grid:
            print(' '.join(row))

    def print_word_list(self):
        """Print the list of words to the terminal."""
        print()
        for word in self.word_list:
            print(word)

    def get_letter(self, row, column):
        """Get the letter contained at a given cell."""
        return self.grid[row][column]

    def solve(self):
        """Solves the word search by locating the positions of all words.

        Iterates over every cell in the grid and, if a possible match is found,
        traverses its neighbours, until all words have been found
        """
        row_index = 0
        while row_index <= len(self.grid):
            for row in self.grid:
                col_index = 0
                for letter in row:
                    # If the cell contains a letter that is the first letter of
                    # one of the words, then traverse all of its neighbours
                    # to see if any longer prefixes can be found.
                    if self.trie.contains_prefix(letter):
                        self.traverse_tiles(letter, row_index, col_index)
                    col_index += 1
                row_index += 1

        # Inform the user if some words haven't been found
        sorted_remaining_words = list(self.remaining_words)
        sorted_remaining_words.sort()
        print('The following words were not found: {}'.format(
              ', '.join(sorted_remaining_words)))

    def traverse_tiles(self, letter, row_index, col_index):

        directions = {'right':    (0, 1),
                      'down-right': (1, 1),
                      'down':       (1, 0),
                      'down-left':  (1, -1),
                      'left':       (0, -1),
                      'up-left':    (-1, -1),
                      'up':         (-1, 0),
                      'up-right':   (-1, 1)}

        for direction_name in directions:
            direction = directions[direction_name]
            prefix = letter
            next_row_index = row_index
            next_col_index = col_index

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

            if not self.remaining_words:
                print("solved!")
                exit()


# Helper functions to build a WordSearch object from input files

def build_grid(filename):
    """Scrape a formatted text file and convert it into a word search grid.

    Args:
        filename: A text file containing rows of alphabetical characters,
            optionally separated by spaces or commas. Each row must contain the
            same number of letters.

    Returns:
        A 2d list, representing the rows and columns of the word search grid.
    """
    grid = []

    input_file = open(filename, 'r')
    for line in input_file.read().splitlines():
        # Ignore separators
        line = line.replace(' ', '')
        line = line.replace(',', '')
        row = list(line)
        grid.append(row)
    input_file.close()

    return grid


def build_word_list(filename):
    """Scrape a text file for the list of words that must be found.

    Args:
        filename: A text file containing a list of comma-separated values.

    Returns:
        A list containing the words that must be found.
    """
    input_file = open(filename, 'r')
    word_list = input_file.read()
    input_file.close()

    # Extract words from a comma-separated list
    word_list = word_list.split(',')

    # Remove leading and trailing spaces from all words
    word_list = [word.strip(' \n') for word in word_list]

    return word_list


def main():
    """Build and solve a sample word search."""
    grid = build_grid('sample_grid.txt')
    word_list = build_word_list('sample_word_list.txt')
    word_search = WordSearch(grid, word_list)

    # word_search.print_grid()
    # word_search.print_word_list()
    # print()

    word_search.solve()


if __name__ == '__main__':
    main()
