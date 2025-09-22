from collections import deque

def wordLadderLength(startWord, targetWord, wordList):
    queue = deque()
    queue.append((startWord, 1))
    st = set(wordList)
    st.discard(startWord)
    
    # N * word length * 26 * log N
    while queue:
        word, steps = queue.popleft()
        if word == targetWord:
            return steps
            
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + ch + word[i+1:]
                if newWord in st:
                    st.remove(newWord)
                    queue.append((newWord, steps+1))
    return 0
    
    
# Test Case
startWord = "hit"
targetWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadderLength(startWord, targetWord, wordList))