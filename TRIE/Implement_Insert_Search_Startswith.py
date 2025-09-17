class Trie:
    # Trie Node
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {} # dictionary of 26 alphabets
        self.isEnd = False # flag
        
    def insert(self, word: str) -> None: # word = "apple"
        """
        Inserts a word into the trie.
        """
        node = self # node = root (we assign root to node here)
        for c in word: # c = a, p, p, l, e
            if c not in node.children: # if a is not present
                node.children[c] = Trie() # create a new node with a, p, p, l, e
            node = node.children[c] # node = node.children[a, p, p, l, e] (here node is pointing to a, p, p, l, e)
        node.isEnd = True # last node (node.children[e] -> flag = True)
        return
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self # node = root
        for c in word: # c = a, p, p, l, e
            if c not in node.children: # if a is not present
                return False
            node = node.children[c] # node = node.children[a, p, p, l, e]
        return node.isEnd # return True
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self # node = root
        for c in prefix: # c = a, p, p
            if c not in node.children: # if a is not present
                return False
            node = node.children[c] # node = node.children[a, p, p]
        return True
    
# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
prefix = "app"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2, param_3)
