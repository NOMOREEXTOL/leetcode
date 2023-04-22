class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        力扣1143题
        744ms,34.8MB
        """

        dp = [[0 for _ in range(len(text1) + 1)] for __ in range(len(text2) + 1)]  # dp数组的含义是dp[i][j]表示text1索引范围0~i-1,text2索引范围0~j-1时的最长公共子序列长度
        # 初始化，dp[0][i] = dp[j][0] = 0
        # 递推公式: if text1[i-1] == text2[j - 1]: dp[j][i] = dp[j-1][i-1] + 1
                    #else: dp[j][i] = max(dp[j-1][i],dp[j][i-1])
        #
        ans = 0

        for i in range(1,len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i - 1],dp[j - 1][i],dp[j][i - 1])
                if dp[j][i] > ans:
                    ans = dp[j][i]
        return ans



    def longestCommonSubsequence2(self):
        """题解,动态规划解法
        672ms,34.7MB
        """

        dp = [[0 for _ in range(len(text1) + 1)] for __ in range(len(text2) + 1)]

        ans = 0

        for i in range(1,len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1  # 为什么是dp[j-1][i-1] + 1呢，因为text1[i-1]和text2[j-1]已经比较过了，避免重复计算，所以递推的时候这两个元素都不能取到因此都要减一
                else:
                    dp[j][i] = max(dp[j - 1][i],dp[j][i - 1]) # 为什么是dp[j-1][i]和dp[j][i-1]，因为若text1[i]和text2[j]没有匹配上，那么还有可能与前面的其他元素匹配上
                    #比如ace和abc当i == 4,j == 4时，e != c,但是abc里面的c是可以与ace里面的c匹配上的，此时对应dp[j][i-1]的情况。反过来同理
                    #与version1相比，为什么不用比较dp[j-1][i-1]: 因为以上两种情况已经包含了dp[j-1][i-1]的情况了，没必要重复计算。这也是为什么不把从dp[0][i]~dp[j-1][i]都比较的原因
                    #dp[j-1][i]正是由前面几项推导过来的，已经包含了这些情况了。
                if dp[j][i] > ans:
                    ans = dp[j][i]
        return ans



if __name__ == '__main__':
    s = Solution()
    # text1 = "ezupkr"
    # text2 = "ubmrapg"
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"

    print(s.longestCommonSubsequence(text1,text2))






