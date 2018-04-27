def isPalindrome(x):
        """
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
        """
        # 1
        return str(x) == str(x)[::-1]
        # Could you solve it without converting the integer to a string?
        # 2
        if x < 0:
            return False
        else:
            return x == (int(str(abs(x))[-1::-1]) * (int(x > 0) - int(x <= 0)))
        # 3
        if x < 0 or x % 10 == 0:
            return False
        elif x > 0 and x < 10:
            return True
        else:
            reversed_x = 0
            while x > reversed_x:
                reversed_x = reversed_x*10 + x % 10
                x //= 10
            return x == reversed_x or x == reversed_x//10


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(110))
