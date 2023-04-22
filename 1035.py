class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        128ms,13.4MB
        力扣1035题 与 1143题相类似
        """
        dp = [[0 for _ in range(len(nums1) + 1)] for __ in range(len(nums2) + 1)]

        ans = 0

        for i in range(1,len(nums1) + 1):
            for j in range(1,len(nums2) + 1):
                if (nums1[i-1] == nums2[j-1]):
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i],dp[j][i-1])
                if dp[j][i] > ans:
                    ans = dp[j][i]
        return ans

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    print(s.maxUncrossedLines(nums1,nums2))





