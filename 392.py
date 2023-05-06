class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        力扣392题,判断子序列
        思路：采用双指针，时间复杂度为O(m+n)
        16ms,13.1MB
        """
        l,r = 0,0
        while (1):
            if l == len(s):
                return True
            if r == len(t):
                return False
            while r < len(t):
                if l < len(s) and s[l] == t[r]:
                    l += 1
                    r += 1
                else:
                    r += 1



    def subSequence2(self,s,t):
        """动态规划解法
        20ms,13.8MB
        """
        l = 0
        dp = [0 for _ in range(len(t))] # dp数组的含义是s[0:l+1]是t[0:i+1]的子串的bool值

        dp[0] = 0 if s[0] != t[0] else 1  # dp数组的初始化
        l = l + 1 if s[0] == t[0] else 0

        for i in range(1,len(t)):
            if l < len(s) and t[i] == s[l]:
                dp[i] = 1
                l += 1
            else:
                dp[i] = dp[i-1]
        return True if dp[i] and l == len(s) else False

    def isSubSequence3(self,s,t):
        """
        动态规划题解
        基本思路为：
        判断两字符串的最长公共子串长度是否为s串的长度
        52ms,15.3MB
        """

        dp = [[0 for __ in range(len(s) + 1)] for _ in range(len(t) + 1)]   # dp数组的含义为: 以i-1和j-1结尾的两字符串的最长公共子序列长度

        for i in range(1,len(t) + 1):
            for j in range(1,len(s) + 1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1] == len(s)


if __name__ == '__main__':
    s = Solution()
    s1 = "abc"
    t1 = "ahbgdc"

    print(s.isSubSequence3(s1,t1))

