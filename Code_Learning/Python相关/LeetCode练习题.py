print("LeetCode的数组排序")
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        nums_len = len(nums)
        while k < nums_len:
            if nums[k] == nums[k - 1]:
                del nums[k]
                nums_len -= 1
            else:
                k += 1
        return nums_len
##############################################################################################################################################################################