class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            if s[l] not in "AEIOUaeiou":
                l+=1
            elif s[r] not in "AEIOUaeiou":
                r-=1
            else:
               s[l],s[r]=s[r],s[l]
               l+=1
               r-=1
        return "".join(s)

                



