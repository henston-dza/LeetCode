class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        sorted_nums = sorted(nums)

        group = {}
        j_idx = {}
        ans = []

        grp = 0
        group[sorted_nums[0]] = grp
        j_idx[grp] = 0

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                grp += 1
                j_idx[grp] = i

            group[sorted_nums[i]] = grp

        i = 0
        while i < n:
            currgrp = group[nums[i]]
            j = j_idx[currgrp]

            ans.append(sorted_nums[j])
            j_idx[currgrp] += 1
            i += 1

        return ans