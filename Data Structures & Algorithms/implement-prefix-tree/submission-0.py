


class PrefixTree:

    class TreeNode:
        def __init__(self):
            self.is_word=False
            self.adj_list=dict()

    def __init__(self):
        self.tree = self.TreeNode()

    def insert(self, word: str) -> None:
        node = self.tree
        for char in word:
            if char not in node.adj_list:
                # letter does not exist
                node.adj_list[char] = self.TreeNode()
            # always update the node
            node = node.adj_list[char]
        # we have added a word record it as a word
        node.is_word=True

    def search(self, word: str) -> bool:
        node = self.tree
        for char in word:
            if char not in node.adj_list:
                return False
            node = node.adj_list[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for char in prefix:
            if char not in node.adj_list:
                return False
            node = node.adj_list[char]
        return True
        