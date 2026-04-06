class Solution(object):
    def judgeCircle(self, moves):
        i,j=0,0
        for o in range(len(moves)):
            n=moves[o]
            if n=='R':
                i+=1
            if n=='L':
                i-=1
            if n=='U':
                j+=1
            if n=='D':
                j-=1
        if i==0 and j==0:
            return True
        else:
            return False