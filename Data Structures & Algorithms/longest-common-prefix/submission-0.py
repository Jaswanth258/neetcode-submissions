class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        reference = strs[0]

        for i in range(len(reference)):
            if not all(
                len(strs[j]) > i and reference[i] == strs[j][i]
                for j in range(len(strs))
            ):
                break

            ans += reference[i]

        return ans