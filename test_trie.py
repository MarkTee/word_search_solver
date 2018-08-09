from trie import *

def test_find_prefix():
    trie = Trie()
    trie.insert_word('dog')
    assert trie.find_prefix('a') == False
    assert trie.find_prefix('d') == True
    assert trie.find_prefix('o') == False
    assert trie.find_prefix('do') == True
