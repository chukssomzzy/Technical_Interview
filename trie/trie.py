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

    def insert(self, word: str) -> None:
        """insert a word to trie"""
        current = self.node
        for cha in word:
            if cha not in current.children:
                current.children[cha] = Node()
                current = current.children[cha]
            elif cha in current.children:
                current = current.children[cha]
        else:
            current.end = True

    def startwith(self, prefix: str) -> bool:
        """Check if a word startwith"""
        current = self.node
        for ch in prefix:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False
        return True

    def contains(self, word: str) -> bool:
        """contains"""
        current = self.node
        for ch in word:
            if ch in current.children:
                current = current.children[ch]
            else:
                return False
        if current.end:
            return True
        return False

