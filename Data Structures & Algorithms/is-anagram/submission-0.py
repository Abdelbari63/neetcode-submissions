class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyS={}
        frequencyT={}
        x = 0
        for char in s:
            if char in frequencyS:
                frequencyS[char]+=1
            else:
                 frequencyS[char]=1

        for char1 in t:
            if char1 in frequencyT:
                frequencyT[char1]+=1
            else:
                frequencyT[char1]=1

        if frequencyS == frequencyT:
            return True
        else:
            return False
