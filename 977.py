class Solution():
    def sortedSquares(self,nums):
        """
        leetcode977:返回平方后的非递减数组
        思路： 类比插入排序
        实测超时
        """

        nums[0] = nums[0] ** 2

        for fast in range(1,len(nums)):
            curVal = (nums[fast]) ** 2
            curInd = fast
            pre = curInd - 1
            while pre >= 0 and nums[pre] > curVal:
                nums[pre + 1] = nums[pre]
                pre -= 1
            nums[pre + 1] = curVal
        return nums


    def sortedSquares2(self,nums):
        """
        v1改进：v1没有充分利用好原数组也是有序的这个条件
        改进方式，已排序数组维护在右边，将左边元素平方之后插入右边
        最坏时间复杂度任然为O(n2)
        """

        endVal = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                endVal = nums[i] ** 2
                break

        nums = [_ ** 2 for _ in nums]

        ind = 0
        while ind < len(nums):
            if ind + 1 < len(nums) and nums[ind] >= nums[ind + 1]:
                curVal = nums[ind]
                curInd = ind + 1
                while curInd < len(nums) and nums[curInd] <= curVal:
                    nums[curInd - 1] = nums[curInd]
                    curInd += 1
                nums[curInd - 1] = curVal
                if nums[0] == endVal:
                    break
            else:
                break
        return nums






    def quick_sort(self,nums):
        def QS(start,end,nums):
            if end <= start:
                return
            low = start
            high = end
            midvalue = nums[start]
            while low < high:
                while low < high and nums[high] >= midvalue:
                    high -= 1
                nums[low] = nums[high]
                while low < high and nums[low] < midvalue:
                    low += 1
                nums[high] = nums[low]
            nums[low] = midvalue
            QS(start,low - 1,nums)
            QS(low + 1,end,nums)
        QS(0,len(nums) - 1,nums)
        return nums

    def sortedSquares2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        先平方再排序，
        264ms,14.8MB(5.24,63.64 %)

        """
        nums = [i ** 2 for i in nums]

        def quick_sort(start, end, nums):
            if end <= start:
                return
            left = start
            right = end
            midvalue = nums[start]
            while left < right:
                while left < right and nums[right] >= midvalue:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] < midvalue:
                    left += 1
                nums[right] = nums[left]
            nums[right] = midvalue
            quick_sort(start, right - 1, nums)
            quick_sort(right + 1, end, nums)

        quick_sort(0, len(nums) - 1, nums)
        return nums


    def sortedSquares3(self,nums):
        """
        针对平方后的数组，从中间值开始，往左和往右都是递增的，故可采用双指针，归并排序的思想
        维护一个双指针从中间向两边扩散，每次将较小的元素插入到新数组当中
        52ms,15MB(30.22,21.22 %)
        """
        divIndex = len(nums) - 1 # 分界点默认放在最后，对应数组当中全是负数的情况，循环遍历第一个为正的值，再退出

        # 找到分界点
        for i in range(len(nums)):
            if nums[i] >= 0:
                if nums[i] ** 2 <= nums[i - 1] ** 2:
                    divIndex = i
                else:
                    divIndex= i - 1
                break

        nums = [_ ** 2 for _ in nums]

        ans = [nums[divIndex]]

        left = divIndex - 1
        right = divIndex + 1
        while left >= 0 and right < len(nums):
            if nums[left] < nums[right]:
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1

        if right == len(nums):
            while left >= 0:
                ans.append(nums[left])
                left -= 1
        if left == -1:
            while right < len(nums):
                ans.append(nums[right])
                right += 1

        return ans




if __name__ == '__main__':
    s = Solution()
    # nums = [-4,-1,0,1,3] # ac
    # nums = [-3,-2,-1] # ac
    # nums = [1,2,3] # ac
    # nums = [-1,2,2] # 针对此测试用例，对v3进行修改，分界点应该取正数和前面一个数绝对值最小的那个
    nums = [1,2,3]
    print(s.sortedSquares3(nums))





    #  快排测试用例
    # nums1 = [7,8,9,6,1,2,8]
    # s.quick_sort(nums1)
    # print(nums1)
