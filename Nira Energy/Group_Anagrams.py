def groupAnagrams(strs):
    if not strs:
        return []

    groups = {}  # key: sorted-string, value: list of anagrams

    for i in range(len(strs)):
        s = strs[i]
        print(s)
        key = ''.join(sorted(s))  # canonical signature for the word
        print("key: ", key)
        if key in groups:
            groups[key].append(s)
            print(groups)
        else:
            groups[key] = [s]

    return list(groups.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))