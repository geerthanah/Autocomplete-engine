from collections import defaultdict
import heapq

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq=1):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True
        node.freq += freq

    def _dfs(self, node, prefix, heap):
        if node.is_end:
            heapq.heappush(heap, (-node.freq, prefix))
        for char, child in node.children.items():
            self._dfs(child, prefix + char, heap)

    def autocomplete(self, prefix, k=5):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        heap = []
        self._dfs(node, prefix, heap)
        return [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]
