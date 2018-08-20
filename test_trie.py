from trie import *

def test_find_prefix():
    trie = Trie()
    trie.insert_word('dog')
    assert trie.find_prefix('a') is None
    assert trie.find_prefix('d') is not None
    assert trie.find_prefix('o') is None
    assert trie.find_prefix('do') is not None
    assert trie.find_prefix('g') is None
    assert trie.find_prefix('dogg') is None
    assert trie.find_prefix('dog') is not None

