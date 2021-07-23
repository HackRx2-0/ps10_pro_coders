class Trie:
    def __init__(self , cache = None):
        """
        Initialize your data structure here.
        """
        if cache is None:
            self.root = dict()
        else:
            self.root = cache

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.root
        
        for ch in word:
            if ch not in temp:
                temp[ch] = dict()
            temp = temp[ch]
        temp['isEnd'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        
        for ch in word:
            if ch not in temp:
                return False
            else:
                temp = temp[ch]
        
        return 'isEnd' in temp

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        
        for ch in prefix:
            if ch not in temp:
                return False
            else:
                temp = temp[ch]
        return True

