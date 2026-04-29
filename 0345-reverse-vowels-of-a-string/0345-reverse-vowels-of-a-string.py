class Solution(object):
    def reverseVowels(self, s):
        a=list(s)
        l,r=0,len(a)-1
        while l<r:
            if a[l] not in "AEIOUaeiou":
                l+=1
            elif a[r] not in "AEIOUaeiou":
                r-=1
            else:
                t=a[l]
                a[l]=a[r]
                a[r]=t
                l+=1
                r-=1
        s="".join(i for i in a)
        return s

                



