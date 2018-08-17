class Trie:
    """A very basic implentation of a trie.

    Only supports adding words and determining whether a given prefix exists
    within it.
    """

    def __init__(self):
        self._head = TrieNode()

    def insert_word(self, word):
        """Adds a word to the trie (as well as all intermediate nodes)."""
        node = self._head
        remaining_letters_index = None

        for index, letter in enumerate(word):
            if letter in node.children:
                node = node.children[letter]
            else:
                remaining_letters_index = index
                break

        # Add nodes for any letters that aren't already present in the trie
        if remaining_letters_index is not None:
            for letter in word[index:]:
                index += 1
                if index == len(word):
                    node.add_child(letter, True)
                else:
                    node.add_child(letter)
                node = node.children[letter]

    def find_prefix(self, prefix):
        """Determines whether a given prefix exists in the trie."""
        node = self._head
        prefix_in_trie = True

        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                prefix_in_trie = False
                break

        return prefix_in_trie


class TrieNode:
    """Represents the nodes of a trie. Nodes don't contain data."""

    def __init__(self, terminal_node=False):
        self._children = {}
        self._terminal_node = terminal_node

    def add_child(self, child, is_terminal_node=False):
        """Adds a descendant (which will have a common prefix) to the node."""
        if is_terminal_node:
            self._children[child] = TrieNode(True)
        else:
            self._children[child] = TrieNode()

    @property
    def children(self):
        return self._children
