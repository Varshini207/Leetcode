class Solution(object):
    def judgeCircle(self, moves):
        r,l,u,d=0,0,0,0
        for i in range(len(moves)):
            n=moves[i]
            if n=='R':
                r+=1
            if n=='L':
                l+=1
            if n=='U':
                u+=1
            if n=='D':
                d+=1
        if l==r and u==d:
            return True
        else:
            return False