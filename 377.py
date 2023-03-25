class Solution():
    def combinationSum4(self,
                        nums:list[int],
                        target:int
                        )->int:
        """力扣377题"""
        dp = [0 for _ in range(target+1)]   #dp数组初始化
        dp[0] = 1

        #本题要求的是排列总数，所以要先遍历背包，再遍历物品
        for j in range(target+1):
            for i in range(len(nums)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j-nums[i]]
        return dp[target]

if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    s = Solution()
    print(s.combinationSum4(nums,target))  #结果为7
