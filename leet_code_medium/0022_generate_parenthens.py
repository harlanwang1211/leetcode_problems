# leetcode 0022 Generte Parenthens (Medium)
# https://leetcode.com/problems/generate-parentheses/description/
def generateParenthesis(n):
    result = []
    for i in range(2**(n*2) + 1):
        j  = str(bin(i))[2:]
        if len(j) < n*2:
            j = '0'*(n*2-len(j)) + j
        j = j.replace('1', '(')
        j = j.replace('0', ')')
        z = j
        if j.count('(') == j.count(')') and '()' in j:
            k = 0
            while k <= n:
                z = z.replace('()', '')
                k += 1
            if len(z) == 0:
                result += [j]
    return result

# test
print (generateParenthesis(3))