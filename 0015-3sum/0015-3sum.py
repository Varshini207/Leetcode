class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        if nums==
        """
        if len(nums)<3:
            return []
        g=[]
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    a=[nums[i],nums[l],nums[r]]
                    if a not in g:
                        g.append(a)
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        
        return g
