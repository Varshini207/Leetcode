class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in nums:
            s.append(i*i)
        s.sort()
        return s

        