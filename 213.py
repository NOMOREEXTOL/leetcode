class Solution():
    def rob(self,nums):
        """
        打家劫舍||，房间成环了，第一个房间和最后一个房间是相邻的。从起点开始，往后迭代，由于最后一个房间和第一个房间认为是
        相邻的，故每个起点的结果有两个，一个是不包含尾节点的最大值，一个是包含尾节点的最大值。这个包含是指，尾节点在考虑的范围之内
        即不一定一定要取尾节点。version1:28ms,13MB
        """
        if len(nums) <= 3:
            return max(nums)
        dpTail = [0 for _ in range(len(nums))]  # 用于保存各节点考虑尾节点的情况下的最大值
        dpNotTail = [0 for _ in range(len(nums))]  # 用于保存各节点不考虑尾节点情况下的最大值

        dpTail[-1] = nums[-1]
        dpTail[-2] = dpNotTail[-2] = nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            for j in range(i + 2, len(nums)):
                if not (i == 0 and j == len(nums) - 1):
                    dpTail[i] = max(dpTail[i], dpTail[j])
                dpNotTail[i] = max(dpNotTail[i], dpNotTail[j])
            dpNotTail[i] += nums[i]
            dpTail[i] += nums[i]
        return max(dpNotTail[0], dpNotTail[1], dpNotTail[2]
                   , dpTail[1], dpTail[2])


    def rob2(self,nums):
        """题解解法，本题与打家劫舍1唯一的区别就是首尾也认为是相连的了，这个环形的不好
        考虑，因为首和尾不能同时选取。线性的往往更容易理解故尝试把环形问题转化成线性问题求解，
        首尾不能同时考虑，归根结底就三种情况既不考虑头也不考虑尾；只考虑头不考虑尾；不考虑头，
        只考虑尾；不能同时考虑头和尾。如数组 1 6 9 6 1,对应上面三种情况则是求6 9 6 ; 1 6 9 6 ; 6 9 6 1;
        三种情况的最大值.这三种情况的求解其实就是和打家劫舍|完全一样了，同时情况三和情况二的最大值其实包含情况一的最大值。
        如此题情况一的最大值为12，情况二和情况三的最大值也为12。但是若数组是100 6 9 6 100的话，MAX1 = 12
        MAX2 = 109, MAX3 = 109。故只需要考虑两种情况就行了。version2:8ms,13.2MB
        """
        if len(nums) == 1:
            return nums[0]
        def robSubproblem(nums):
            """封装打家劫舍|的代码,返回对应范围数组的最大值，最后比较两种情况返回值的最大值即可"""
            if len(nums) <= 2:
                return max(nums)
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-2] + nums[i],dp[i-1])
            return dp[len(nums)-1]

        return max(robSubproblem(nums[1:]),robSubproblem(nums[:-1]))


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.rob2(nums))




