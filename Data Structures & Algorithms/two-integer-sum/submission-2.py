class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = {}
        list2 = []
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in list1:
             list2 = [list1[complement],i]
            else:
                list1[nums[i]] = i
        return list2
