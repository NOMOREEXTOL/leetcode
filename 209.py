class Solution():
    def minSubArrayLen(self,nums,target):
        """
        尝试双指针求解
        思路：慢指针slow固定不动，快指针fast向后移动，直到区间总和大于sum停下，更新区间最小长度，
        慢指针slow向后移动，当区间总和大于sum时，更新最小长度，直到区间总和小于sum,再继续移动fast，直到fast移动到最后。
        36ms,19.4MB(77.21,71.62 %)
        """
        if len(nums) == 0 or target == 0:
            return 0
        if sum(nums) < target:
            return 0

        slow = 0
        curSum = nums[0]
        minLens = len(nums)
        fast = 1
        while fast < len(nums):
            if (curSum < target):
                curSum += nums[fast]
                fast += 1
            else:
                while (slow < fast and curSum >= target):
                    if (fast - slow < minLens):
                        minLens = fast - slow
                    curSum -= nums[slow]
                    slow += 1

        while (slow < fast and curSum >= target):
            if (fast - slow < minLens):
                minLens = fast - slow
            curSum -= nums[slow]
            slow += 1

        return minLens



if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 7
    print(s.minSubArrayLen(nums,target))



