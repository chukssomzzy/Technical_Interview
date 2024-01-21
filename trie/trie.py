#!/usr/bin/env python3
"""Trie datastructure"""


from typing import Dict, List, Union


class Node:
    """Node"""
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    """Trie"""
    def __init__(self):
        self.node = Node()

    def insert(self, word):
        """insert a word to trie"""
        current = self.node
        for cha in word:
            if cha not in current:
                self.node[cha] = Node()
