class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEndOfWord=False
        self.children=[None]*26
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr=self
        for c in word:
            if(curr.children[ord(c)-ord('a')]==None):
                curr.children[ord(c)-ord('a')]=Trie()
            curr=curr.children[ord(c)-ord('a')]
        curr.isEndOfWord=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr=self
        for c in word:
            curr=curr.children[ord(c)-ord('a')]
            if (curr==None):
                return False
        if (curr.isEndOfWord):
            return True
        return False
            
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr=self
        for c in prefix:
            curr=curr.children[ord(c)-ord('a')]
            if (curr==None):
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

