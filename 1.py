class Solution():
    def twoSum(self,nums,target):
        """
        leetcode1:两数之和hash表解法
        20ms,13.8MB(86.56,52.22 %)
        """
        ans = []
        midDict = dict()
        midDict[nums[0]] = 0

        for i in range(1,len(nums)):
            needValue = target - nums[i]
            if needValue in midDict:
                ans.append(i)
                ans.append(midDict[needValue])
                return ans
            else:
                midDict[nums[i]] = i






if __name__ == '__main__':
    pass