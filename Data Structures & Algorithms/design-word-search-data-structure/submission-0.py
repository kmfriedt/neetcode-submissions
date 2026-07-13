class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.is_word=False
            self.children=dict()

    def __init__(self):
        self.tree = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.tree
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]

        node.is_word=True

    def search(self, word: str) -> bool:
        node = self.tree

        return self.dfs(word, node)

    def dfs(self, sub_string: str, node: TrieNode):
        if len(sub_string) == 0 and node.is_word:
            return True

        for i in range(len(sub_string)):
            char=sub_string[i]
            if char == '.':
                for nextNode in node.children.values():
                    if self.dfs(sub_string[i+1:], nextNode):
                        return True
                return False
            elif char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word

