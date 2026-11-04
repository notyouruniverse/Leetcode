class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        new_list = []

        x = len(nums) - k

        for m in nums[x:]:
            new_list.append(m)

        for i in nums[:x]:
            new_list.append(i)

        nums[:] = new_list