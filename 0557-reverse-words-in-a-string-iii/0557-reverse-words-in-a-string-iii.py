class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w=s.split()
        r=[]
        for u in w:
            i=list(u)
            l=0
            q=len(i)-1
            while l<q:
                i[l],i[q]=i[q],i[l]
                l+=1
                q-=1
            r.append("".join(i))
        return (" ".join(r))