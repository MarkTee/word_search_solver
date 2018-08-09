class Trie:
    """A very basic implentation of a trie that only supports adding words and determining whether a given prefix exists within it."""

    def __init__(self):
        self._head = TrieNode()

    def insert_word(self, word):
        """Adds a word as a terminal node to the trie (as well as all intermediate nodes)."""
        node = self._head
        terminal_node = True

        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                terminal_node = False
                break

        if not terminal_node:
            while i < len(word):
                node.add_child(word[i])
                node = node.children[word[i]]
                i += 1

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

    def __init__(self):
        self._children = {}

    def add_child(self, child):
        """Adds a descendant (which will have a common prefix) to the current node."""
        self._children[child] = TrieNode()

    @property
    def children(self):
        return self._children
