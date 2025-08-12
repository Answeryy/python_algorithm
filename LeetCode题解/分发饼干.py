class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = count = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                i += 1
                count += 1
            j += 1
        return count        

