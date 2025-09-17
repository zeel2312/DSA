def characterReplacement(s, k):
    l = 0 # left pointer
    counts = {} # dict
    best = 0
    
    for r in range(len(s)):
        counts[s[r]] = 1 + counts.get(s[r], 0)
        
        while (r-l+1) - max(counts.values()) > k: # window_size - maxfreq > k
            counts[s[l]] -= 1 # shrink from left
            l += 1 # increment left pointer
        best = max(best, r-l+1) # keep the track of best(max) window size
    return best
 
s = "ABAB"
k = 2
print(characterReplacement(s,k))