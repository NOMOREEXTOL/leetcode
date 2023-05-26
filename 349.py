class Solution():
    def intersection(self,nums1,nums2):
        """
        leetcode349
        双指针解法
        24ms,13MB(57.95,90.75 % )
        """
        nums1.sort()
        nums2.sort()

        ans = []

        left = right = 0

        while (left < len(nums1) and right < len(nums2)):
            if (nums1[left] == nums2[right]):
                ans.append(nums1[left])
                left += 1
                right += 1
                while (left < len(nums1) and nums1[left - 1] == nums1[left]):
                    left += 1
                while (right < len(nums2) and nums2[right - 1] == nums2[right]):
                    right += 1
            elif (nums1[left] < nums2[right]):
                while (left < len(nums1) and nums1[left] < nums2[right]):
                    left += 1
            else:
                while (right < len(nums2) and nums2[right] < nums1[left]):
                    right += 1

        return ans


    def intersection2(self,nums1,nums2):
        """
        解法二：hash表
        24ms,13.1MB(57.95,62.98 %)
        """
        hashList = [0] * 1001

        for i in nums1:
            if hashList[i] == 0:
                hashList[i] += 2

        for j in nums2:
            if hashList[j] == 2:
                hashList[j] -= 1

        ans = []
        for item in range(len(hashList)):
            if hashList[item] == 1:
                ans.append(item)
        return ans




    

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(s.intersection2(nums1,nums2))