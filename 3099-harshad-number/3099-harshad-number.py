class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
       a=0
       s=x
       while(x!=0):
        a+=x%10
        x/=10
    
       if s%a==0:
        return a
       else:
        return -1

        