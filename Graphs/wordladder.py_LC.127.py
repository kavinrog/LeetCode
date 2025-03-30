from collections import deque
def wordladder(beginWord, endWord, wordList):
    
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0 
    
    q = deque([(beginWord, 1)])
    visited = set([beginWord])
    
    while q:
        word, step = q.popleft()
        if word == endWord:
            return step
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = word[:i] + c + word[i+1:]
                if nextWord in wordSet and nextWord not in visited:
                    visited.add(nextWord)
                    q.append((nextWord, step +1))
    return 0 