class Solution():
    def search(self,nums,target):
        """
        二分查找算法
        28ms,19.7MB(47.75,5.01)
        """
        def binarysearch(start,end):
            if end - start == 1:
                if nums[end] == target:
                    return end
                if nums[start] == target:
                    return start
                return -1
            if end == start:
                return end if nums[end] == target else -1
            l = start
            r = end
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarysearch(l,mid - 1)
            else:
                return binarysearch(mid + 1,r)
        return binarysearch(0,len(nums) - 1)






if __name__ == '__main__':
    s = Solution()
    nums = [2,5]
    target = 0
    print(s.search(nums,target))