class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {} # dictionary of 26 alphabets
        self.EndWith = 0
        self.cntPrefix = 0
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self # node = root (we assign root to node here)
        for c in word: # c = a, p, p, l, e
            if c not in node.children: # if a is not present
                node.children[c] = Trie() # create a new node with a, p, p, l, e
            node = node.children[c] # node = node.children[a, p, p, l, e] (here node is pointing to a, p, p, l, e)
            node.cntPrefix += 1
        node.EndWith += 1 # last node (node.children[e] -> flag = True) 
        return
        
    def countWordsEqualTo(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self # node = root
        for c in word: # c = a, p, p, l, e
            if c not in node.children: # if a is not present
                return 0
            node = node.children[c] # node = node.children[a, p, p, l, e]
        return node.EndWith
        
    def countWordsStartingWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self # node = root
        for c in prefix: # c = a, p, p
            if c not in node.children: # if a is not present
                return 0
            node = node.children[c] # node = node.children[a, p, p]
        return node.cntPrefix
    
    # We assume that the word is already present
    def erase(self, word: str) -> None:
        """
        Erases a word from the trie.
        """
        node = self # node = root
        for c in word: # c = a, p, p, l, e
            if c not in node.children: # if a is not present
                return
            node = node.children[c] # node = node.children[a, p, p, l, e]
            node.cntPrefix -= 1
        node.EndWith -= 1
        
# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
prefix = "app"
obj.insert(word)
obj.insert(word)
obj.erase(word)
param_2 = obj.countWordsEqualTo(word)
param_3 = obj.countWordsStartingWith(prefix)
print(param_2, param_3)