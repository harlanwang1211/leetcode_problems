def isValid(s):
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    """
    while len(s) > 0:
        if '[]' not in s and '{}' not in s and '()' not in s:
            return False
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return True

#test
print(isValid(''))
print(isValid("(([]){})"))
print(isValid('{}([])'))
