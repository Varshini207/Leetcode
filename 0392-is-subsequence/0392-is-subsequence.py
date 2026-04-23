class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=0
        if len(s)==0:
             return True
        else:
            for r in range(len(t)):
                if s[l]==t[r]:
                    l+=1
                if l==len(s):
                    return True
                
            return len(s)==l
        