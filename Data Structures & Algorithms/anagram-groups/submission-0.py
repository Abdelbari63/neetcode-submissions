class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        sort = {}
        for word in strs:
            group = []
            a = tuple(sorted(word))
            if a in sort:
                sort[a].append(word)
            else:
                sort[a] = [word]
        
        final = [value for value in sort.values()]
        return final
