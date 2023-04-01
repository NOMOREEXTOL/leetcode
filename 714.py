class Solution():
    def maxProfit(self,prices,fee):
        """买卖股票的最大利润含手续费，
        股票买卖可以无限次，但是每次买卖都要付固定的手续费
        基本思路是：与无限购买差不多，只不过每次卖出的话利益要少fee罢了
        version1:204ms,17.3MB
        """
        dp = [0,0] #dp[0]表示持有股票的最大利润，dp[1]表示不持有股票的最大利润
        dp[0] = -prices[0]

        for i in range(1,len(prices)):
            dp[0] = max(dp[0],dp[1] - prices[i])
            dp[1] = max(dp[1],dp[0] + prices[i] - fee)  #再卖出股票的时候再减去手续费，可以理解为，完成了一笔交易才需要付手续费
        return dp[1]

   
if __name__ == "__main__":
    s = Solution()
    prices = [1,3,7,5,10,3]
    fee = 3
    print(s.maxProfit(prices,fee))