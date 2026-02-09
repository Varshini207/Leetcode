class Solution(object):
    def checkPerfectNumber(self, num):
        c=1
        if num<=1:
            return False
        i=2
        while i*i<num:
            if num%i==0:
                c+=i
                if i*i!=num:
                    c+=num//i
            i+=1
        return c==num
