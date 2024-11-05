class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0 
            char = word[index]
            if char not in node.children:
                return False
            should_delete_current_node = _delete(node.children[char], word, index + 1)

            if should_delete_current_node:
                del node.children[char]
                return len(node.children) == 0  
            return False

        _delete(self.root, word, 0)

# Example usage
trie = Trie()
trie.insert("hello")
trie.insert("hell")
trie.insert("heaven")
trie.insert("heavy")

print("Search for 'hello':", trie.search("hello"))  
print("Search for 'hell':", trie.search("hell"))    
print("Search for 'heaven':", trie.search("heaven"))  
print("Search for 'he':", trie.search("he"))        

trie.delete("hello")
print("Search for 'hello' after deletion:", trie.search("hello")) 
