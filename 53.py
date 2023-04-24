class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        120ms,22.4MB,贪心算法,当和小于零时丢弃前面所有
        """
        maxVal = max(nums)
        curMax = 0
        for i in nums:
            if i + curMax <= 0:
                curMax = 0
                continue
            else:
                curMax = curMax + i
            if curMax > maxVal:
                maxVal = curMax
        return maxVal


    def maxSubArray2(self,nums):
        """动态规划算法
        196ms,25.9MB
        """
        n = max(nums)
        if n > 0:
            dp = [0 for i in range(len(nums) + 1)] # dp数组的含义是从0到i-1(必须以i-1结尾)的最大数组和
        else:
            dp = [n for i in range(len(nums) + 1)]


        ans = n

        for i in range(1,len(nums) + 1):
            if nums[i-1] + dp[i-1] > 0:  # 当前值与前面一个集合的值相加，如果大于零则更新，最后判断更新的值是否大于ans
                dp[i] = dp[i-1] + nums[i-1]
            if dp[i] > ans:
                ans = dp[i]
        return ans


    def maxSubArray3(self,nums):
        """动态规划题解 + 状态压缩
        100ms,21.5MB
        """

        dp = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            dp = max(dp + nums[i],nums[i]) # 递推公式分为两种情况，取之前的和，以及从i处截断重新开始计算
            if dp > ans:
                ans = dp
        return ans


    def maxSubArray4(self,nums):
        """尝试双指针解法
        ac173/210        """
        pre = 0
        cur = len(nums) - 1
        ans = sum(nums)
        curMax = sum(nums)
        while pre < cur:
            if nums[pre] < nums[cur]:
                curMax -= nums[pre]
                pre += 1
                if curMax > ans:
                    ans = curMax
            elif nums[pre] > nums[cur]:
                curMax -= nums[cur]
                cur -= 1
                if curMax > ans:
                    ans = curMax
            else:
                if pre < cur and nums[pre + 1] < nums[cur - 1]:
                    curMax -= nums[pre]
                    pre += 1
                    if curMax > ans:
                        ans = curMax
                elif pre < cur and nums[pre + 1] > nums[cur - 1]:
                    curMax -= nums[cur]
                    cur -= 1
                    if curMax > ans:
                        ans = curMax
                else:
                    break
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
    print(s.maxSubArray4(nums))






