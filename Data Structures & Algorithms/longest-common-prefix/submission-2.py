class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        out = ""

        for x in range(len(strs)):
            if len(strs[x]) < l:
                l = len(strs[x])

        for i in range(l):
            match = True

            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    match = False
                    break

            if match:
                out += strs[0][i]
            else:
                break

        return out