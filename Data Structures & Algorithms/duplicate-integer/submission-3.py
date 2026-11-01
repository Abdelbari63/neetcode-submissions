class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False

"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i != j:
                   if nums[i]==nums[j]:
                       a+=1
                   

        if a != 0:
          return True
        else:
            return False
            """