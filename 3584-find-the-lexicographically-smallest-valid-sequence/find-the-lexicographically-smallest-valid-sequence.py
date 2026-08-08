class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        nxtIdx = [[-1] * 26 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            nxtIdx[i] = nxtIdx[i + 1].copy()
            nxtIdx[i][ord(word1[i]) - ord('a')] = i

        suff = [-1] * m

        k = m - 1

        for i in range(n - 1, -1, -1):
            if k < 0:
                break

            if word1[i] == word2[k]:
                suff[k] = i
                k -= 1

        ans = []

        i = 0
        j = 0
        Used = False

        while i < n and j < m:
            idx = nxtIdx[i][ord(word2[j]) - ord('a')]

            if Used:
                if idx == -1:
                    return []

                if j < m - 1 and suff[j + 1] <= idx:
                    return []

                ans.append(idx)
                i = idx + 1
                j += 1

            else:
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    j += 1

                elif j == m - 1 or (
                    suff[j + 1] != -1 and i < suff[j + 1]
                ):
                    Used = True
                    ans.append(i)
                    i += 1
                    j += 1

                else:
                    i += 1

        if len(ans) == m:
            return ans

        return []