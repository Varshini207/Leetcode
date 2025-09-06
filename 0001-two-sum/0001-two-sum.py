class Solution:
  def twoSum(self, nums,target):
    seen = {}   # dictionary to store value : index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:   # check if we’ve already seen the complement
            return [seen[diff], i]
        seen[num] = i
    return []
