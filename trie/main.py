#!/usr/bin/env python3

"""Testing trie"""
from trie import Trie

trie = Trie()
trie.insert("apple")
trie.insert("adp")
trie.insert('app')

current = trie.node.children

print(current['a'].children['p'].children['p'].end)
print(trie.startwith('as'))
print(trie.contains('ad'))
print(trie.contains('app'))
