class Solution(object):
    def reverseString(self,s):
        l=0
        r=len(s)-1
        while l<(len(s)/2)+1 and r>(len(s)/2)-1:
            t=s[l]
            s[l]=s[r]
            s[r]=t    
            l+=1
            r-=1 