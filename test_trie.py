from trie import *

def test_find_prefix():
    trie = Trie()
    trie.insert_word('dog')
    assert trie.contains_prefix('a') == False
    assert trie.contains_prefix('d') == True
    assert trie.contains_prefix('o') == False
    assert trie.contains_prefix('do') == True
    assert trie.contains_prefix('g') == False
    assert trie.contains_prefix('dogg') == False

