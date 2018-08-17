class Trie:
    """A very basic implentation of a trie

    Supports adding words and determining whether a given prefix exists within
    the Trie.
    """

    def __init__(self):
        self.head = TrieNode()

    def insert_word(self, word):
        """Adds a word (and all of the prefixes that it contains) to the trie."""
        node = self.head
        remaining_prefixes = None

        # Traverse the tree until a prefix that isn't contained in the trie is found
        for index, letter in enumerate(word):
            if letter in node.children:
                node = node.children[letter]
            else:
                remaining_prefixes = index
                break

        # Add nodes for any prefixes that aren't already present in the trie
        if remaining_prefixes is not None:
            for letter in word[remaining_prefixes:]:
                node.add_child(letter)
                node = node.children[letter]

    def contains_prefix(self, prefix):
        """Determines whether a given prefix exists in the trie."""
        current_node = self.head
        prefix_in_trie = True

        for letter in prefix:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                prefix_in_trie = False
                break

        return prefix_in_trie


class TrieNode:
    """Represents the nodes of a trie

    Nodes don't contain data as they're referred to by the keys in their
    parent node's dictionaries.
    """

    def __init__(self):
        self._children = {}

    def add_child(self, child):
        """Adds a descendant (which shares a common prefix) to the given node."""
        self._children[child] = TrieNode()

    @property
    def children(self):
        return self._children
