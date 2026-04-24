class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s=''
        l=0
        r=0
        while l<len(word1) and r<len(word2):
           # if len(word1)>len(word2):
            if l<len(word1):
                s+=word1[l]
                l+=1
            if r<len(word2):
                s+=word2[r]
                r+=1
        s+=word1[l:]
        s+=word2[r:]
            
        
        return s
                