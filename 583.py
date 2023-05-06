class Solution():
    def minDistance(self,word1,word2):
        """
        :param word1:
        :param word2:
        :return:
        leetcode583题
        思路：version1
        求最长公共子串，则步数ans = 两串总长度 - 2 * 公共子串长度
        即求两字符串的最长公共子串长度（连续）
        """

        dp = [[0 for __ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        # dp数组的含义是word1以i-1为结尾，word2以j-1为结尾的最长公共连续子串长度为dp[i][j]
        # 递推公式为:  if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        #             else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        # maxLength = dp数组的最大值

        maxLength = 0
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                if dp[j][i] > maxLength:
                    maxLength = dp[j][i]
        print(maxLength)
        return len(word1) + len(word2) - 2 * maxLength


    def minDistance2(self,word1,word2):
        """
        :param word1:
        :param word2:
        :return:
        version2:
        v1存在逻辑漏洞，如果word1 = park,word2 = ppake,则结果应为3而不是5
        修改逻辑为，把连续子串改成非连续最长子串即可。
        180ms,15.1MB(67.82,88.12)

        """

        dp = [[0 for _ in range(len(word1) + 1)] for __ in range(len(word2) + 1)]
        # dp数组的含义是: word1 0~i-1 与 word2 0 ~ j - 1的最长非连续子串长度为dp[j][i]
        # 步数ans = len(word1) + len(word2) - 2 * maxSubLength
        # maxSubLength = dp[-1][-1]
        # 递推公式为 if word1[i-1] == word2[j-1]: dp[j][i] = dp[j-1][i-1] + 1
        #           else: dp[j][i] = max(dp[j-1][i],dp[j][i-1])


        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]




if __name__ == '__main__':
    s = Solution()
    word1 = "leetcode"
    word2 = "etcode"
    print(s.minDistance2(word1,word2))


