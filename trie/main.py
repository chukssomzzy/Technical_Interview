#!/usr/bin/env python3

"""Testing trie"""
from trie import Trie

trie = Trie('apple', 'apps')

print(trie.node['l'].node)
