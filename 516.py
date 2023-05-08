class Solution():
    def longestPalindromeSubseq(self, s):
        """
        先考虑暴力解法

        """

        def isPalindrome(targetStr):
            l = 0
            r = len(targetStr) - 1
            while l < r:
                if targetStr[l] != targetStr[r]:
                    return False
                l += 1
                r -= 1
            return True

        maxLength = 0

        for length in range(len(s), 0, -1):
            flag = False
            l = 0
            r = l + length
            while r < len(s) + 1:
                midStr = s[l:r]
                if isPalindrome(midStr) and len(midStr) > maxLength:
                    maxLength = len(midStr)
                    flag = True
                    break
                l += 1
                r += 1
            if flag:
                break
        return maxLength
        # 只能解出最长连续的回文子序列


    def longestPalindromeSubseq2(self,s):
        """
        动态规划解法
        1256ms,28.5MB(28.57,19.6 %)
        """
        dp = [[0 for _ in range(len(s))] for __ in range(len(s))]
        # dp数组的含义是i~j的闭区间段，最长非连续回文子序列长度为dp[i][j]
        # 递推公式为 if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
        #           else: dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        # 对于遍历顺序，由于dp[i][j] 是由 dp[i + 1][j - 1],dp[i + 1][j],dp[i][j - 1]推导出来的
        # 故遍历顺序一定是i倒序，j正序

        maxLength = 1
        # 遍历顺序
        for i in range(len(s) - 1,-1,-1):
            for j in range(i,len(s)):
                if i == j:  # 顺便初始化
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2  # 如果两端的元素相等，那么新区间最长的非连续回文子串长度就是在原区间的基础上加2
                    else: # 如果两端元素不相等，那么新区见最长非连续回文子串的长度就应该在两端分别去掉一个元素的基础上的最大值，由于dp[i][j - 1],dp[i + 1][j]之前已经求出来的，所以是可行的。
                        dp[i][j] = max(dp[i][j - 1],dp[i + 1][j])
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
        return maxLength










if __name__ == '__main__':
    s = Solution()
    s1 = "cbbd"
    print(s.longestPalindromeSubseq2(s1))