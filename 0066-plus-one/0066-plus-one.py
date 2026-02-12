class Solution:
    def plusOne(self, digits):
        c=0
        l=[]
        for i in range(len(digits)):
            c=(c*10)+digits[i]
        c+=1
        s=str(c)
        for i in range(len(s)):
            l.append(int(s[i]))
        
        return l



      