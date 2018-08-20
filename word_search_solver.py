#!/usr/bin/env python3
from trie import Trie


class WordSearch:
    """Contains all relevant information for solving a particular word search,
    including:

    - Puzzle grid
    - Word list (and its corresponding trie)
    - Methods to display and solve the word search

    Attributes:
        directions: A dictionary mapping the names of the eight directions
            (used when traversing the grid) to their corresponding coordinate
            vectors of the following form: (change_in_row, change_in_column).

        grid: A 2d list representing the word search's grid.
        self.rows, self.cols: The dimensions of the word search' grid; the
            grid will always be rectangular.
        word_list: A list representation of all the words that need to be
            found; this value should remain static.
        remaining_words: A set containing the words that have not yet been
            found by the solver.
        solutions: A dictionary that maps found words to tuples of the
            following format: (starting_cell, direction).
        trie: A trie made up of the words contained in the word list.
    """

    directions = {'right':    (0, 1),
                  'down-right': (1, 1),
                  'down':       (1, 0),
                  'down-left':  (1, -1),
                  'left':       (0, -1),
                  'up-left':    (-1, -1),
                  'up':         (-1, 0),
                  'up-right':   (-1, 1)}

    def __init__(self, grid, word_list):
        """Inits a WordSearch object.

        - Separates the word list into those that have been found and those
        that remain hidden.

        - Builds a trie representing the WordSearch's words.
        """
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

        self._word_list = word_list
        self.remaining_words = set(word_list)
        self.solutions = {}
        for word in self._word_list:
            self.solutions[word] = None

        self.trie = Trie()
        self.build_trie()

    def build_trie(self):
        """Populates the trie with all words from the word list."""
        for word in self._word_list:
            self.trie.insert_word(word)

    def print_puzzle(self):
        """Prints the grid and the list of words to the terminal."""
        print("=" * 72)
        print("Puzzle")
        print("=" * 72)
        print()
        for row in self.grid:
            print(' '.join(row))
        print()
        for word in self._word_list:
            print(word)
        print()

    def print_solutions(self):
        """Prints all solutions to the terminal."""
        print("=" * 72)
        print("Solutions")
        print("=" * 72)
        width = len(max(self._word_list,
                        key=len)) + 1  # width of the longest word plus padding
        for word in self._word_list:
            if self.solutions[word] is None:
                print("{:{width}} - "
                      "Could not be found".format(word, width=str(width)))
            else:
                # Add 1 to each coordinate as it will be clearer for the user.
                row_index = self.solutions[word][0][0] + 1
                col_index = self.solutions[word][0][1] + 1
                direction = self.solutions[word][1]
                print("{:{width}} - Row {:>2}, Column {:>2}, moving {}".format(
                      word, row_index, col_index, direction, width=str(width)))

    def get_letter(self, row, column):
        """Get the letter contained at a given cell."""
        return self.grid[row][column]

    def solve(self):
        """Solves the word search by locating the positions of all words.

        Locates all words by iterating over every cell in the grid, and, if a
        possible match is found, traverses that cell's neighbours to build
        larger prefixes.
        """
        row_index = 0
        for row in self.grid:
            col_index = 0
            for letter in row:
                # If the cell contains a letter that is the first letter of
                # one of the words, then traverse all of its neighbours (in
                # all directions) to see if any longer prefixes can be
                # found.
                if self.trie.find_prefix(letter) is not None:
                    for direction in WordSearch.directions:
                        self.traverse_tiles(letter, row_index,
                                            col_index, direction)
                        if not self.remaining_words:  # if all words are found
                            return
                col_index += 1
            row_index += 1

    def traverse_tiles(self, prefix, row_index, col_index, direction):
        """Traverses the grid and builds prefixes.

        Longer prefixes are built by concatenating neighbouring cells in a
        given direction. Traversal continues until either a word or an invalid
        prefix is found.

        Args:
            prefix: Initially the prefix will always be a single letter (found
                at the starting cell).
            row_index, col_index: The grid coordinates from which traversal
                should start.
            direction: A key from the WordSearch.directions class attribute
                that's used to represent the direction in which the traversal
                should be carried out.
        """
        next_row_index = row_index
        next_col_index = col_index
        change_in_row = WordSearch.directions[direction][0]
        change_in_col = WordSearch.directions[direction][1]
        previous_node = None

        while True:
            # To improve search times, we won't look up each prefix from the
            # root. Since we know all previous prefixes exist, we only need to
            # look at the last character of the prefix, and can start the
            # search from the last known node.
            previous_node = self.trie.find_prefix(prefix[-1],
                                                  starting_node=previous_node)
            if previous_node is not None:
                if prefix in self.remaining_words:
                    self.remaining_words.remove(prefix)
                    # Mark a solution as having been found
                    self.solutions[prefix] = ((row_index, col_index), direction)
                    if not self.remaining_words:  # yeords are found
                        return

                # If a valid prefix is found, continue to traverse the grid in
                # the given direction
                next_row_index += change_in_row
                next_col_index += change_in_col
                # If an edge of the grid is about to be crossed, then stop
                if 0 <= next_row_index < self.rows and \
                   0 <= next_col_index < self.cols:
                    prefix += self.get_letter(next_row_index, next_col_index)
                else:
                    return
            else:
                return  # if the new prefix doesn't exist in the trie


# Helper functions to build a WordSearch object from input files

def build_grid(filename):
    """Scrapes a formatted text file and converts it into a word search grid.

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
    """Scrapes a text file for the list of words that must be found.

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
    """Builds and solves a sample word search."""
    grid = build_grid('sample_grid2.txt')
    word_list = build_word_list('sample_word_list2.txt')
    word_search = WordSearch(grid, word_list)

    word_search.solve()
    word_search.print_puzzle()
    word_search.print_solutions()


if __name__ == '__main__':
    main()
