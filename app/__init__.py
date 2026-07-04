from collections import Counter

wordBank = "../dictionary.txt"

# testStr = "MALLEY"
testStr = "BEERZED"
# testStr = "FACADE"
# testStr = "SILTTID"
# testStr = "TRTHAO"

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

def makeTrie(filename):
    trie = Trie()
    with open(filename) as f:
        for line in f:
            word = line.strip().upper()
            if word:
                trie.insert(word)
    return trie

def printTrie(node, prefix=""):
    if node.isWord:
        print(prefix)
    for char, child in node.children.items():
        printTrie(child, prefix + char)

def searchTrie(node, available, prefix, res):
    if node.isWord:
        res.append(prefix)
    for char, child in node.children.items():
        if available[char] > 0:
            available[char] -= 1
            searchTrie(child, available, prefix + char, res)
            available[char] += 1

heads = Counter(testStr)
wordTrie = makeTrie(wordBank)
possibleWords = []

for letter in sorted(set(testStr)):
    if letter in wordTrie.root.children:
        heads[letter] -= 1
        searchTrie(wordTrie.root.children[letter], heads, letter, possibleWords)
        heads[letter] += 1

print(possibleWords)