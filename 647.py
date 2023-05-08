class Solution():
    def countSubStrings(self,s):
        """
        leetcode647题，求回文子串数目
        先考虑暴力解法
        6332ms,13.2MB(5.19,84.81%) 通过
        """

        def isSubString(strJudge):
            l,r = 0,len(strJudge) - 1
            while l < r:
                if strJudge[l] != strJudge[r]:
                    return False
                l += 1
                r -= 1
            return True


        count = len(s) # 初始回文子串数目设置为字符个数
        for length in range(2,len(s) + 1):
            l = 0
            r = l + length
            while r <= len(s):
                midStr = s[l:r]
                if isSubString(midStr):
                    count += 1
                l += 1
                r += 1
        return count



    def countSubstrings2(self,s):
        """
        动态规划解法
        思路： 每次只需要比较两端的元素就行了，若两端元素相同且中间子串为回文串，则整个就是回文串
        328ms,21.5MB
        """
        dp = [[0 for _ in range(len(s))] for __ in range(len(s))]
        # dp数组的含义是 [i,j]段（左闭右闭）是否为回文串,若是则dp[i][j] = True 否则为False

        # 递推公式为 if s[i] == s[j]:dp[i][j] = dp[i+1][j-1]
        #           else:   dp[i][j] = False

        # 初始化dp数组，当i == j时为True
        for i in range(len(s)):
            dp[i][i] = 1

        ans = len(s) # 用于保存回文串数量
        # 遍历
        for length in range(1,len(s)):    # 打印dp数组发现要从主对角线向右上方遍历
            i = 0
            j = i + length
            while j < len(s):
                if length == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        ans += 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                        if dp[i][j]:
                            ans += 1
                i += 1
                j += 1

        # 关于遍历顺序，方式二：由于dp[i][j] 是依赖于dp[i + 1][j - 1]推导而来的，所以遍历顺序也可为
        # for i in range(len(s) - 1,-1,-1):
        #    for j in range(i,len(s)):

        # for i in range(len(s) - 1, -1, -1):
        #     for j in range(i, len(s)):
        #         if s[i] == s[j]:
        #             if j - i <= 1:
        #                 dp[i][j] = 1
        #                 ans += 1
        #             else:
        #                 dp[i][j] = dp[i + 1][j - 1]
        #                 if dp[i][j]:
        #                     ans += 1

        for i in range(len(s)):
            print(dp[i])
        return ans



    def countSubstrings3(self,s):
        """
        尝试双指针解法
        思路为：
        遍历每一个单元素作为中心点，依次向左右拓展，当遇到左右不相等时直接break进入下一个中心点
        统计回文子串数目
        72ms,13.2MB (86.5,62.17 %)
        """
        ans = len(s) # 用于统计回文子串个数

        # 统计长度大于等于2的且长度为偶数的回文子串个数
        for i in range(0,len(s) - 1):
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

        # 统计长度大于2的,长度为奇数的回文子串个数
        for center in range(1,len(s) - 1): # 中心点的可取范围是第二个元素至倒数第二个元素
            l = center - 1
            r = center + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break
        return ans






if __name__ == "__main__":
    s = Solution()
    str1 = "aaaaa"
    print(s.countSubstrings3(str1))
