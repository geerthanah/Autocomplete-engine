from core.trie import Trie

class AutoCompleteEngine:
    def __init__(self):
        self.trie = Trie()

    def load_words(self, filepath):
        with open(filepath, 'r') as f:
            for line in f:
                word = line.strip()
                if word:
                    self.trie.insert(word)

    def get_suggestions(self, prefix, k=5):
        return self.trie.autocomplete(prefix, k)
