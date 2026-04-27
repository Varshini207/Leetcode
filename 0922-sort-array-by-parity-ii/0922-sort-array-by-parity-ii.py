class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        o,e=[],[]
        for i in nums:
            if i%2!=0:
                o.append(i)
            else:
                e.append(i)
        l,r=0,0
        for i in range(len(nums)):
            if i%2!=0:
                nums[i]=o[l]
                l+=1
            else:
                nums[i]=e[r]
                r+=1
        return nums
