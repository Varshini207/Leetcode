class Solution(object):
    def findContentChildren(self, g, s):
        l,r,c=0,0,0
        g=sorted(g)
        s=sorted(s)
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                c+=1
                l+=1
                r+=1
            elif g[l]>s[r]:
                r+=1
            
        return c
            