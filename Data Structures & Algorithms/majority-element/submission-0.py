class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fr = {}
        n = len(nums)
        for num in nums:
            if num in fr:
                fr[num] += 1
            else:
                fr[num] = 1

        for k,v in fr.items():
            if v > n//2:
                return int(k)