class Solution():
    def removeElement(self,nums,val):
        """
        leetcode27题，原位删除数组当中的元素
        只能使用常量空间
        8ms,13.3MB
        """
        l = -1
        r = l + 1
        while r < len(nums):
            if nums[r] == val:
                l += 1
                while r < len(nums) and nums[r] == val:
                    r += 1
                if r == len(nums):
                    return l
                nums[l],nums[r] = nums[r],nums[l]
                r = l + 1
            else:
                l += 1
                r += 1
        return l + 1

    def removeElement2(self,nums,target):
        """
        双指针优化

        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != target:
                nums[slow] = nums[fast]
                slow += 1
        return slow











if __name__ == '__main__':
    s = Solution()
    nums = [2,2]
    val = 3
    print(s.removeElement2(nums,val))
