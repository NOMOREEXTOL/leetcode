"""通过本题可以顺便提出01背包问题的最小硬币问题，只需要把遍历背包的顺序由正序改成倒序就行了。"""



class Solution():

    def coinChange(self,coins,amount):
        """力扣322题，零币兑换问题，动态规划解法，转化成完全背包问题"""
        dp = [[0,0] for _ in range(amount+1)] #因为这题不仅要判断是否可以兑换，而且还要求出兑换的最小硬币数量
        #所以二维数组0号位表示当前的最大价值，1号位表示，取得当前价值所用的最小硬币数，其实如果每次取得是前一位最大的，
        #那么用的硬币数肯定也是最少的了

        for i in range(len(coins)):#先遍历物品再遍历背包
            for j in range(coins[i],amount+1):
                if dp[j][0] >= dp[j-coins[i]][0] + coins[i]:
                    dp[j][0] = dp[j][0]
                else:
                    dp[j][0] = dp[j-coins[i]][0] + coins[i] #取了本层的硬币，则要在上一层的基础上加一
                    dp[j][1] = dp[j-coins[i]][1] + 1

        if dp[amount][0] == amount:
            return dp[amount][1]
        else:
            return -1



    def coinChange2(self,coins,amount):
        """题解"""
        dp = [(2**31) for _ in range(amount+1)] #dp数组的含义是，背包容量为j时，填满背包所需要的最小硬币数为dp[j]，
        #因此递推公式为dp[j] = min(dp[j-coins[i]]+1,dp[j])  取本层硬币和不取本层硬币的最小值。因为要取得是最小值，故
        #dp数组的初始化时，非0下标的值应该初始化成INT_MAX，否则会把实际的硬币数覆盖掉。

        dp[0] = 0

        for i in range(len(coins)):  #这里是先遍历物品再遍历背包，因为本题要求的是最小硬币数，所以无关是组合还是排列，他们最终结果都一样
            #所以这里无论是先遍历物品再遍历背包，还是先遍历背包再遍历物品，都是可以的。
            for j in range(coins[i],amount+1): #遍历背包时为正序遍历，因为这是完全背包问题，如果是倒序遍历的话，就是01背包问题求构成所需
                #所需要的最小硬币数了
                dp[j] = min(dp[j],dp[j-coins[i]]+1)

        if dp[amount] != 2**31:
            return dp[amount]
        else:
            return -1

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    s = Solution()
    print(s.coinChange2(coins,amount))







