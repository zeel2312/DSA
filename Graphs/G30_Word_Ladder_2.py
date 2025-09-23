from collections import deque

def findSequences(startWord, targetWord, wordList):
    queue = deque()
    queue.append(([startWord])) # ['bat']
    st = set(wordList) # {pat, bot, pot, poz, coz}
    usedOnLevel = [startWord] # ['bat']
    level = 0
    ans = []
    
    # N * word length * 26 * log N
    while queue:
        vec = queue.popleft() # path so far # vec = ['bat']
        print("vec: ", vec)
        # Erase all words that has been used in the previous levels to transform
        if len(vec) > level: # yes
            level = len(vec) # level = 1
            for w in usedOnLevel: # 'bat'
                st.discard(w) # {this stays the same}
            usedOnLevel = [] # convert to empty list once you move a level up
    
        word = vec[-1] # bat
        if word == targetWord: # no
            if len(ans) == 0: # first case where we reached the end
                ans.append(vec)
            elif len(ans[0]) == len(vec):
                ans.append(vec)
            continue
                
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + ch + word[i+1:] # aat, bat, cat ... pat, bot
                if newWord in st: # no
                    print("newWord: ", newWord)
                    newPath = list(vec) # ['pat']
                    newPath.append(newWord) # ['bat','pat']
                    queue.append(newPath) # ['bat','pat']
                    usedOnLevel.append(newWord) # mark as visited on the level ['pat']
    return ans
    
    
# Test Case
startWord = "bat"
targetWord = "coz"
wordList = ["pat", "bot", "pot", "poz", "coz"]
print(findSequences(startWord, targetWord, wordList))