class Solution(object):
    def twoSum(self, nums, target):
        n=[]
        l=len(nums)
    
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    n.append(i)
                    n.append(j)
                   
        return (n)
