class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = sorted(nums)
        n=x[len(nums)//2]
        return n 
        