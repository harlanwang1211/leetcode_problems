def longestCommonPrefix(strs):
    if [] in strs or strs == []:
        return ""
    min_len = len(strs[0])
    min_num = 0
    for i in range(len(strs)):          # find the shortest string's lenth and position
        if len(strs[i]) < min_len:
            min_len = len(strs[i])
            min_num = i
    for k in range(min_len):
        for h in strs:
            if h[k] != strs[min_num][k]:
                if k == 0:
                    return "" # if th first letter of each string is differnet, return ""
                else:
                    return strs[min_num][0:k]
    return strs[min_num]
# test data
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["abab","aba",""]))
print(longestCommonPrefix(["abab"]))
print(longestCommonPrefix(["c", "c", "c"]))
print(longestCommonPrefix(["cc", "cc"]))
print(longestCommonPrefix(["aa", "ab"]))
print(longestCommonPrefix(["aaa", "aa"]))
