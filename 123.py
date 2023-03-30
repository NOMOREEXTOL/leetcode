"""
version2，对于从右到左遍历求单次购买的最大值算法，其合理性测试代码如下
def maxProfit(prices):
    dp = [[0,0] for _ in range(len(prices))]
    dp[-1][0] = prices[-1]
    for i in range(len(prices)-2,-1,-1):
        dp[i][0] = max(dp[i+1][0],prices[i])
        dp[i][1] = max(dp[i+1][1],dp[i+1][0] - prices[i])
    return dp[0][1]


def maxProfit2(prices):
    if len(prices) == 0 or len(prices) == 1:
        return 0

    dp = [0, 0]  # 与之前一样，dp[0]表示持有股票的最大利润，dp[1]表示不持有股票时的最大利润
    dp[0] = -prices[0]
    for i in range(1, len(prices)):
        dp[0] = max(dp[0], -prices[i])
        dp[1] = max(dp[1], dp[0] + prices[i])
    return dp[1]

if __name__ == "__main__":
    import random
    for i in range(2000):
        prices = []
        for i in range(random.randint(1,30)):
            prices.append(random.randint(1,100))
        if maxProfit(prices) != maxProfit2(prices):
            print(prices)

测试用例2000个，可以认为通过。

"""




class Solution():
    def maxProfit(self,prices):
        """买卖股票最大利润3
        买卖股票的最大利润2可以无限次的购买，
        买卖股票1只能购买一次，而3是只能购买2次，因此基本想法是，将两次分开来看，因为每次购买都不能同时进行
        所以可以将区间划分为两个部分，求划分的最大值，每一部分相当于是一个买卖股票1的结果
        时间复杂度为O(n2),实测超时，通过用例202。
        """

        def subProfit(prices):
            if len(prices) == 0 or len(prices) == 1:
                return 0

            dp = [0,0] #与之前一样，dp[0]表示持有股票的最大利润，dp[1]表示不持有股票时的最大利润
            dp[0] = -prices[0]
            for i in range(1,len(prices)):
                dp[0] = max(dp[0],-prices[i])
                dp[1] = max(dp[1],dp[0] + prices[i])
            return dp[1]

        maxpro = 0
        for j in range(-1,len(prices)):
            prof1 = subProfit(prices[:j+1])
            prof2 = subProfit(prices[j+1:])
            if prof2 + prof1 > maxpro:
                maxpro = prof1 + prof2
        return maxpro


    def maxProfit2(self,prices):
        """对Version1进行优化，分为两个dp数组，一个从左到右购买一次的最大利润，一个从右到左的最大利润，每次比较两个dp交界处和的最大值
        时间复杂度为O(n),version2:636ms,47.5MB
        """
        dp1 = [[0,0] for _ in range(len(prices))] #从左到右只购买一次股票所得到的最大值
        dp2 = [[0,0] for __ in range(len(prices))] #从右到左只购买一次股票所得到的最大值

        dp1[0][0] = -prices[0]
        dp2[-1][0] = prices[-1]

        for i in range(1,len(prices)):
            dp1[i][0] = max(dp1[i-1][0],-prices[i])
            dp1[i][1] = max(dp1[i-1][1],dp1[i-1][0] + prices[i])

        for j in range(len(prices) - 2,-1,-1):
            dp2[j][0] = max(dp2[j+1][0],prices[j])
            dp2[j][1] = max(dp2[j+1][1],dp2[j+1][0] - prices[j])

        maxprof = dp2[0][1] #只买一次的最大值
        for mid in range(len(prices)-1):
            if dp1[mid][1] + dp2[mid+1][1] > maxprof:
                maxprof = dp1[mid][1] + dp2[mid+1][1]

        return maxprof

    def maxProfit3(self,prices):
        """题解，动态规划解法,version3:540ms,37.4MB,可在此基础之上再利用滚动数组优化空间复杂度"""
        dp = [[0,0,0,0,0] for _ in range(len(prices))] #dp数组的含义是dp[i][0] 表示第i天不操作所得到的最大值
        #dp[i][1]表示第i天第一次持有股票所获得的最大利润,dp[i][2]表示第i天第一次不持有股票所获得的最大利润。
        #dp[i][3]表示第i天第二次持有股票时所获得的最大利润，dp[i][4]表示第i天第二次不持有股票时所获得的最大利润

        #递推公式为
        # dp[i][0] = dp[i-1][0]
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i]) #继续保持之前持有的状态，或者前面几天是不操作的状态，然后在第i天购入
        # dp[i][2] = max(dp[i-1][2],dp[i-1][1] + prices[i]) #继续保持之前第一次不持有的状态，或者就在今天卖了。
        # dp[i][3] = max(dp[i-1][3],dp[i-1][2] - prices[i]) #继续保持之前第二次持有的状态，或者就在今天买，那么前面几天的状态必须是第一次不持有股票
        # dp[i][4] = max(dp[i-1][4],dp[i-1][3] + prices[i]) #继续保持之前第二次不持有的状态，或者就在今天卖第二次。



        #初始化
        dp[0][0] = 0#第一天不操作，利润自然是0
        dp[0][1] = -prices[0] #第一天第一次持有股票就是买入
        dp[0][2] = 0 #第一天第一次不持有股票，最终利润肯定也是0，相当于第一天买了然后马上又卖了
        dp[0][3] = -prices[0] #第一天第二次持有股票相当于第一次卖了之后又买入股票
        dp[0][4] = 0 #相当于做两次买了又卖

        for i in range(1,len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i]) #继续保持之前持有的状态，或者前面几天是不操作的状态，然后在第i天购入
            dp[i][2] = max(dp[i-1][2],dp[i-1][1] + prices[i]) #继续保持之前第一次不持有的状态，或者就在今天卖了。
            dp[i][3] = max(dp[i-1][3],dp[i-1][2] - prices[i]) #继续保持之前第二次持有的状态，或者就在今天买，那么前面几天的状态必须是第一次不持有股票
            dp[i][4] = max(dp[i-1][4],dp[i-1][3] + prices[i])

        return dp[-1][4]    #直接返回第二次不持有的最大利润就行了，因为这种情况其实包含了第一次不持有的最大利润
        # ，因为如果第一次不持有的最大利润最大，那么在此基础之上，买了又卖就相当于第二次不持有的最大利润了，结果是一样的。

    def maxProfit4(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        在3基础之上采用滚动数组优化，324ms,21.5MB
        """
        dp = [0, 0, 0, 0, 0]  # dp数组的含义是dp[i][0] 表示第i天不操作所得到的最大值
        # dp[i][1]表示第i天第一次持有股票所获得的最大利润,dp[i][2]表示第i天第一次不持有股票所获得的最大利润。
        # dp[i][3]表示第i天第二次持有股票时所获得的最大利润，dp[i][4]表示第i天第二次不持有股票时所获得的最大利润

        # 递推公式为
        # dp[i][0] = dp[i-1][0]
        # dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i]) #继续保持之前持有的状态，或者前面几天是不操作的状态，然后在第i天购入
        # dp[i][2] = max(dp[i-1][2],dp[i-1][1] + prices[i]) #继续保持之前第一次不持有的状态，或者就在今天卖了。
        # dp[i][3] = max(dp[i-1][3],dp[i-1][2] - prices[i]) #继续保持之前第二次持有的状态，或者就在今天买，那么前面几天的状态必须是第一次不持有股票
        # dp[i][4] = max(dp[i-1][4],dp[i-1][3] + prices[i]) #继续保持之前第二次不持有的状态，或者就在今天卖第二次。

        # 初始化
        dp[0] = 0  # 第一天不操作，利润自然是0
        dp[1] = -prices[0]  # 第一天第一次持有股票就是买入
        dp[2] = 0  # 第一天第一次不持有股票，最终利润肯定也是0，相当于第一天买了然后马上又卖了
        dp[3] = -prices[0]  # 第一天第二次持有股票相当于第一次卖了之后又买入股票
        dp[4] = 0  # 相当于做两次买了又卖

        for i in range(1, len(prices)):
            dp[0] = dp[0]
            dp[1] = max(dp[1], dp[0] - prices[i])  # 继续保持之前持有的状态，或者前面几天是不操作的状态，然后在第i天购入
            dp[2] = max(dp[2], dp[1] + prices[i])  # 继续保持之前第一次不持有的状态，或者就在今天卖了。
            dp[3] = max(dp[3], dp[2] - prices[i])  # 继续保持之前第二次持有的状态，或者就在今天买，那么前面几天的状态必须是第一次不持有股票
            dp[4] = max(dp[4], dp[3] + prices[i])

        return dp[4]  # 直接返回第二次不持有的最大利润就行了，因为这种情况其实包含了第一次不持有的最大利润
        # ，因为如果第一次不持有的最大利润最大，那么在此基础之上，买了又卖就相当于第二次不持有的最大利润了，结果是一样的。


if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    s = Solution()
    print(s.maxProfit3(prices))

