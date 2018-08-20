class Trie:
    """A very basic implentation of a trie

    Supports adding words and determining whether a given prefix exists within
    the Trie.

    Attributes:
        root: The topmost/starting node of the trie.
    """

    def __init__(self):
        self._root = TrieNode()

    def insert_word(self, word):
        """Adds a word (and all its prefixes) to the trie."""
        node = self._root
        remaining_prefixes = None

        # Traverse the tree until a new prefix is found
        for index, letter in enumerate(word):
            if letter in node.children:
                node = node.children[letter]
            else:
                remaining_prefixes = index
                break

        # Add nodes for any prefixes that aren't already present in the trie
        if remaining_prefixes is not None:
            for letter in word[remaining_prefixes:]:
                index += 1
                if index == len(word):
                    node.add_child(letter, terminal_node=True)
                else:
                    node.add_child(letter)
                node = node.children[letter]

    def contains_prefix(self, prefix):
        """Determines whether a given prefix exists in the trie.

        Returns:
            A boolean value stating whether or not the prefix has been found.
        """
        current_node = self._root

        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False

        return True

    @property
    def root(self):
        return self._root


class TrieNode:
    """Represents the nodes of a trie

    Nodes don't contain data as they're referred to by keys (which will be a
    single letter) in their parent node's dictionaries.

    Attributes:
        children: A dictionary containing the descendant nodes that share a
            common prefix.
        terminal_node: Denotes whether or not a node is a leaf of the trie.
    """

    def __init__(self, terminal_node=False):
        self._children = {}
        self._terminal_node = terminal_node

    def add_child(self, child, terminal_node=False):
        """Adds a descendant to the given node."""
        self._children[child] = TrieNode(terminal_node)

    def is_terminal_node(self):
        return self._terminal_node

    @property
    def children(self):
        return self._children
