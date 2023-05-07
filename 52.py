class Solution():
    def minDistance(self,word1,word2):
        """
        编辑距离
        leetcode52
        思路为：求出最长非连续公共子序列，则
        ans = max(len(word1),len(word2)) - maxSubLength

        不对，如word1 = "intention",word2 = "execution"，预期结果为 5 而不是4
        """
        dp = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]
        # dp数组的含义是 word1的 0 ~ i - 1段，word2的0 ~ j - 1段的最长公共子序列长度为dp[i][j]
        # 递推公式为 if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        #           else:    dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])

        for i in range(1,len(word1) + 1):
            for j in range(1,len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])
        return max(len(word1),len(word2)) - dp[-1][-1]



    def minDistance2(self,word1,word2):
        """
        version2
        思路为：先去二者最长连续子序列，去掉这个子序列，再求剩下部分的最长连续子序列
        则ans = 1 + max(len(word1),len(word2)) - maxRemainLength
        """
        # 先求最长连续子序列

        def maxSubLength(w1,w2):
            dp = [[0 for _ in range(len(w2) + 1)] for __ in range(len(w1) + 1)]

            maxLength = -1
            maxIndex1 = -1
            maxIndex2 = -1

            for i in range(1,len(w1) + 1):
                for j in range(1,len(w2) + 1):
                    if w1[i-1] == w2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
                        maxIndex1 = i  # 不包括下标元素i
                        maxIndex2 = j  # 不包括下标元素j

            return maxLength,maxIndex1,maxIndex2

        maxLength,maxIndex1,maxIndex2 = maxSubLength(word1,word2) # 先求出最长公共连续子序列
        if maxLength == -1: # 说明最长公共子序列为0
            return max(len(word1),len(word2))

        # 去掉最长公共子串
        nextWord1 = word1.replace(word1[maxIndex1 - maxLength:maxIndex1],"")
        nextWord2 = word2.replace(word2[maxIndex2 - maxLength:maxIndex2],"")

        return 1 + max(len(nextWord1),len(nextWord2)) - maxSubLength(nextWord1,nextWord2)[0]

    def minDistance3(self,word1,word2):
        """
        动态规划解法
        120ms,16.4MB (39.75,19.37 % )

        """
        dp = [[0 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]
        # dp数组的含义是 word1的0 ~ i -1段, word2 的 0 ~ j -1 段，二者相互转换所需要的最小操作数
        # 递推公式为 if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
        #           else: dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1] + 1,dp[i-1][j-1] + 1) # 前两项对应删除操作，后一项对应替换操作
        # 如何理解dp[i-1][j-1] + 1？ 如 word1 = "or" ,word2 = "oa" ,此时r != a,但是要把word1 转化为 word2 只需要一步（即替换r或者a），而不是两步(先删除r再删除a)
        # dp[i-1][j] + 1和dp[i][j-1] + 1 是分别包含删除i和删除j的情况的，同时删除i和j的情况也各自包含了。
        # 至于增加的操作，由于删除和添加实质上的步数是一样的，如word1 = "a" ,word2 = "ab"，那么word2删除b可得word1，word1添加b可得word2



        # 初始化
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for j in range(len(word2) + 1):
            dp[0][j] = j

        # 遍历
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,dp[i][j-1] + 1,dp[i-1][j-1] + 1)
        return dp[-1][-1]







if __name__ == '__main__':
    s = Solution()
    word1 = "intention"
    word2 = "execution"
    print(s.minDistance3(word1,word2))



