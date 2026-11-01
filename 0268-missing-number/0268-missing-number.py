class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = len(nums)
        for i in range(0, temp + 1):
            if i not in nums:
                return i
        