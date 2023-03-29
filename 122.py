class Solution():
    def maxProfit(self,prices):
        """在每一天，你可以决定是否购买和/或出售股票,与买卖股票1不同的地方是，买卖股票1
        从头到尾只能买一次，而这个则可以买卖多次,24ms,13.8MB
        """
        dp = [0,0] #dp数组的含义与买卖股票1相同，即dp[0]表示持有股票状态的最大值，dp[1]表示不持有股票状态的最大值
        #dp数组初始化形式也一样
        dp[0] = - prices[0]

        #递推公式有区别
        # 由于买卖股票1只能买一次股票，所以在买股票之前的总利润都是0，所以，买股票的时候，取得是0-prices[i]
        # 而本题与1的区别就是股票能买卖多次，那么每次买股票时的总利润应该是之前天数通过买卖股票积累下来的利润，所以为dp[i-1][1] - prices[i]

        for i in range(1,len(prices)):
            dp[0] = max(dp[0],dp[1] - prices[i])    #非滚动数组则为dp[i][0] = max(dp[i-1][0],dp[i-1][1] - prices[i])
            dp[1] = max(dp[1],dp[0] + prices[i])    #非滚动数组则为dp[i][1] = max(dp[i-1][1],dp[i-1][0] + prices[i])  dp[i][1]情况与买卖股票1完全相同
            #两个max含义大概理解为：1.如果在今天买入股票所得的价值比在今天以前买入股票还低，那还不如保持不变
            #                      2.如果在今天卖出股票得到的利润，不如在后面几天再卖，那还不如先不卖。
        return dp[1]



if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))




