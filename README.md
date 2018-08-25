# Word Search Solver
This program solves word searches by using tries and depth-first search.

# Usage

To solve an example word search:

> $ python word_search_solver.py examples/grid.txt examples/word_list.txt

To solve your own word search (be sure to specify the paths to your input files):

> $ python word_search_solver.py grid_file word_list_file

Text files containing the word search grid and the list of words to be found 
can be passed through to the program.

Each line in the grid file represents a row of the word search puzzle. Letters 
can optionally be separated by spaces or commas.

The list of words should be a list of comma-separated values.

**Caveats:** This program will only solve rectangular word searches (i.e. each 
row should contain the same number of letters). As is standard in most word 
search puzzles, each word should be at least two letters long, only occur in 
the grid once, and not be contained within a larger word (e.g. *able* can be 
found in vari*able*).

# Author
[Mark Thomas](https://github.com/https://github.com/marktee)

# License
Distributed under the MIT license. See `LICENSE` for details.
