class Solution():
    def maxProfit(self,prices):
        """买卖股票的最佳时机,version1:188ms,20.4MB"""
        dp = [0 for _ in range(len(prices))]   #dp数组的含义是从i到数组最后部分（包括i）的最大值为dp[i]
        #则递推公式为dp[i] = max(prices[i],dp[i+1]) 意思是，如果i当前的值不大于从i往后的部分的最大值
        #那么就算把i这个位置加入也不会影响最大值，否则最大值更新为i当前的值,所以初始化dp[-1] = prices[-1]
        #遍历顺序为从右到左更新
        dp[-1] = prices[-1]
        for i in range(len(prices)-2,-1,-1):  #这样只用了线性时间就可以求出以各下标为起点的部分最大值
            dp[i] = max(prices[i],dp[i+1])

        ans = 0
        for j in range(0,len(prices)-1): #以每一个点为最小值，求其右边的最大值与当前值的差值，最大值即为所求
            midValue = dp[j+1] - prices[j]
            if midValue > ans:
                ans = midValue
        return ans

    def maxProfit2(self, prices):
        """买卖股票的最佳时机,version2:180ms,20.7MB
        在Version1的基础之上进行优化，边求各自下标的最大值，边求以当前下标为买进时间的利润
        """
        dp = [0 for _ in range(len(prices))]  # dp数组的含义是从i到数组最后部分（包括i）的最大值为dp[i]
        # 则递推公式为dp[i] = max(prices[i],dp[i+1]) 意思是，如果i当前的值不大于从i往后的部分的最大值
        # 那么就算把i这个位置加入也不会影响最大值，否则最大值更新为i当前的值,所以初始化dp[-1] = prices[-1]
        # 遍历顺序为从右到左更新
        dp[-1] = prices[-1]
        ans = 0
        for i in range(len(prices) - 2, -1, -1):  # 这样只用了线性时间就可以求出以各下标为起点的部分最大值
            dp[i] = max(prices[i], dp[i + 1])
            midValue = dp[i+1] - prices[i]
            if midValue > ans:
                ans = midValue
        return ans


    def maxProfit3(self,prices):
        """题解，动态规划状态转移求解,version3:392ms,31.7MB"""
        dp = [[0,0] for _ in range(len(prices))] #dp数组的含义是dp[i][0]表示当前状态持有股票的最大价值(包含就从当前天数购入股票的情况)
        #dp[i][1]表示当前状态不持有股票的最大价值(包含就在当前天数把股票卖出的情况)
        #dp数组的定义最终还是基于，对于某一天i，到底买还是不买，卖还是不卖，但是如果简单的定义，每一天买，卖，已经买了还未卖，已经卖了，这四种情况就太多了
        #所以可以一个二维数组表示以上四种状态。
        #递推公式如下：dp[i][0] = max(dp[i-1][0],-prices[i]) (包含两种情况，一个是这一天不购入股票，继续保持，以及就在这一天购入股票，前面几天都没买，那么此时的最大价值就是-prices[i]
        #             dp[i][1] = max(dp[i-1][1],dp[i-1][0] + prices[i]) (包含两种情况，一个是这一天不卖出股票,而是在前面的天数就已经卖了，这一天保持手里没有股票的状态
        #以及，就在这一天把股票卖了，那么此时的价值就是 前一天持有这只股票状态的最大值 + prices[i],既然是这一天卖的，那么前面几天一定是持有的)


        #初始化
        dp[0][0] = -prices[0] #第0天想要计算持有股票的最大值，那么直接就在这一天买就行，计算不持有股票的最大值，就是0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1] #最后肯定是不持有股票的状态的最大价值最大。


    def maxProfit4(self,prices):
        """题解，动态规划状态转移求解,version4，288ms,19.7MB

        滚动数组优化空间,观察二维dp数组，发现递推公式只与前一项有关，故采用滚动数组优化
        """
        dp = [0,0] #dp数组的含义是dp[i][0]表示当前状态持有股票的最大价值(包含就从当前天数购入股票的情况)
        #dp[i][1]表示当前状态不持有股票的最大价值(包含就在当前天数把股票卖出的情况)
        #dp数组的定义最终还是基于，对于某一天i，到底买还是不买，卖还是不卖，但是如果简单的定义，每一天买，卖，已经买了还未卖，已经卖了，这四种情况就太多了
        #所以可以一个二维数组表示以上四种状态。
        #递推公式如下：dp[i][0] = max(dp[i-1][0],-prices[i]) (包含两种情况，一个是这一天不购入股票，继续保持，以及就在这一天购入股票，前面几天都没买，那么此时的最大价值就是-prices[i]
        #             dp[i][1] = max(dp[i-1][1],dp[i-1][0] + prices[i]) (包含两种情况，一个是这一天不卖出股票,而是在前面的天数就已经卖了，这一天保持手里没有股票的状态
        #以及，就在这一天把股票卖了，那么此时的价值就是 前一天持有这只股票状态的最大值 + prices[i],既然是这一天卖的，那么前面几天一定是持有的)


        #初始化
        dp[0] = -prices[0] #第0天想要计算持有股票的最大值，那么直接就在这一天买就行，计算不持有股票的最大值，就是0

        for i in range(1,len(prices)):
            dp[0] = max(dp[0],-prices[i])
            dp[1] = max(dp[1],dp[0]+prices[i])
        return dp[1] #最后肯定是不持有股票的状态的最大价值最大。


if __name__ == "__main__":
    s = Solution()
    prices = [1,2]
    print(s.maxProfit4(prices))










