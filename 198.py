"""
动态规划与递归有点相似，递归思考的是本层如何利用下一层返回的功能实现向上一层提供同样的功能
而动态规划则是思考，本次结果如何由前几次结果而得到，有可能本次结果是由规模更小的同一个问题组成的
比如这题的version1，要求以j为起点的最大值，则要求以j+2，j+3...len(nums)-1为起点的最大值,以此类推。
而version2，要求考虑从0到i的最大值，则要求从0到i-2或者从0到i-1的最大值，而求i-2，i-1的最大值也是同样的问题
"""


class Solution():
    def rob(self,nums):
        """
        :param nums:List[int]
        :return:int
        力扣198题打家劫舍。version1:16ms,12.9MB
        """
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))] #dp数组的含义是以j为起点开始往后抢，所能抢到的最大价值
        #所以递推公式为dp[j] = nums[j] + max(dp[j+2],dp[j+3],....dp[len(nums)-1]),所以最后返回的是max(dp[0],dp[1])
        for i in range(len(nums)-1,-1,-1):  #先遍历起点，再遍历房子
            for j in range(i+2,len(nums)):
                dp[i] = max(dp[i],dp[j])
            dp[i] += nums[i]

        return max(dp[0],dp[1])


    def rob2(self,nums):
        """动态规划问题，题解解法,version2:16ms,12.9MB"""
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))] #dp数组的含义为，考虑从i往前的房子，其最大价值为dp[i]
        #注：这里的考虑，包含两种情况，偷下标为i的房子，以及不偷下标为i的房子，如果偷的话，那么下标为i-1的房子就不再考虑范围之内了
        #如果不偷，则dp[i]实质上就等于dp[i-1]，故递推公式为dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) #初始化，对于下标大于1的值，可以初始化为任意值，因为遍历顺序是从前往后遍历，最后都会覆盖

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[len(nums)-1]




if __name__ == "__main__":
    s = Solution()
    nums = [2,7,9,3,1]
    print(s.rob2(nums))



