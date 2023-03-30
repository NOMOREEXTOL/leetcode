class Solution():
    def maxProfit(self,k,prices):
        """买卖股票最佳时机4,这次既不是无穷次也不是一次了，而是指定次数的k次,那其实和1次，2次的情况是一样的，只是
        把次数换成k罢了,version1:100ms,15.4MB"""
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]

        for i in range(1,2 * k + 1):
            if i % 2 == 1:
                dp[0][i] = -prices[0]

        for j in range(1,len(prices)):
            for m in range(1,2 * k + 1):
                if m % 2 == 1:
                    dp[j][m] = max(dp[j-1][m],dp[j-1][m-1] - prices[j])
                else:
                    dp[j][m] = max(dp[j-1][m],dp[j-1][m-1] + prices[j])
        return dp[-1][2 * k]

    def maxProfit2(self,k,prices):
        """买卖股票最佳时机4,这次既不是无穷次也不是一次了，而是指定次数的k次,那其实和1次，2次的情况是一样的，只是
        把次数换成k罢了,滚动数组优化,version2:88ms,13MB"""
        dp = [0] * (2 * k + 1)

        for i in range(1,2 * k + 1):
            if i % 2 == 1:
                dp[i] = -prices[0]

        for j in range(1,len(prices)):
            for m in range(1,2 * k + 1):
                if m % 2 == 1:
                    dp[m] = max(dp[m],dp[m-1] - prices[j])
                else:
                    dp[m] = max(dp[m],dp[m-1] + prices[j])
        return dp[2 * k]


if __name__ == "__main__":
    s = Solution()
    prices = [3,2,6,5,0,3]
    print(s.maxProfit2(2,prices))
