class Solution(object):
    def reverseString(self,s):
        #return s.reverse()==True
        a=len(s)-1
        b=0
        m=len(s)//2
        while b!=m:
            t=s[b]
            s[b]=s[a]
            s[a]=t
            a-=1
            b+=1
        return s