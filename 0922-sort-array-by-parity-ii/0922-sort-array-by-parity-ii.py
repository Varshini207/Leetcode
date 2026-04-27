class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r=0,1
        n=len(nums)
        while l<n and r<len:
            if nums[l]%2==0:
                l+=2
            elif nums[r]%2==1:
                r+=2
            else:
                nums[l],nums[r]=nums[r],nums[l]

          
        return nums