class Solution(object):
    def isPalindrome(self, x):
        X=str(x)
        c=0
        if (X==X[::-1]):
            c=True
        else:
            c=(False)
        return c