class Solution():
    def lenghtOfLIS(self,nums):
        """最长递增子序列,version:1920ms,13.4MB"""
        dp = [1] * len(nums)    #dp数组的含义为以nums[i]为结尾的最长递增子序列长度为dp[i]
        #dp数组的初始化应该初始化成1，就取当前元素的话，最长递增子序列的长度就为1


        maxLength = dp[0] # 用于保存最长递增子序列的长度,因为dp数组的含义是，以nums[i]为结尾的最长递增子序列的长度。
        # 而最长的递增子序列不一定包含nums[i]，所以要遍历dp数组求，最大值。

        #递推公式为dp[i] = max(dp[j]+1,dp[i]) j从0到i遍历数组，如果发现nums[j] < nums[i]，那么相当于发现了一个[0,i]以内的一个递增
        #子序列,注意，i和j并不一定相邻。此时，由于已经直到dp[j]的大小，那么如果nums[j] < nums[i]的话，dp[i]的一个可能取值就是dp[j]+1
        #由于从0到i，有若干的j，所以就要去求满足条件的里面的最大值。

        for i in range(1,len(nums)): #先遍历每一个下标。
            for j in range(0,i): #再遍历[0,i]段以求区间内部的长度的最大值，遍历顺序从前往后或者从后往前都是可以的，因为求得是
                #每种情况的最大值，而每一个dp[j]已经在上几轮dp[i]中求出来了。
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i],dp[j]+1)
            if dp[i] > maxLength:
                maxLength = dp[i]

        return maxLength

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lenghtOfLIS(nums))