class Solution():
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        力扣718最长公共子数组
        思路：
        1.从其中一个数组中循环遍历每个元素
        2.在另外一个数组中寻找这一个元素，没找到的话就是0，
        3. 找到了则lengthMid = 1，i，j分别记录两个数组的位置，开始依次向后确认对应元素是否相等，若相等则lengthmid++
        当遇到第一个不相等时，或者i，j越界时退出，更新最长序列长度。

        最坏时间复杂度为O(n**3),实测超时

        """
        if len(nums1) == 0 or len(nums2) == 0:
            return 0
        ans = 0

        for i in range(len(nums1)):
            if ans > len(nums1) - i:
                break
            targetVal = nums1[i]
            for j in range(len(nums2)):
                if nums2[j] == targetVal:
                    up = i + 1
                    down = j + 1
                    lengthMid = 1
                    while up < len(nums1) and down < len(nums2):
                        if nums1[up] == nums2[down]:
                            lengthMid += 1
                        else:
                            break
                        up += 1
                        down += 1
                    if lengthMid > ans:
                        ans = lengthMid
        return ans


    def findLength2(self,nums1,nums2):
        """题解动态规划解法
        1708ms,34.9MB
        """
        dp = [[0 for _ in range(len(nums1) + 1)] for __ in range(len(nums2) + 1)] # dp数组的含义为dp[i][j] 表示nums1以i-1，nums2以j-1为结尾的最长公共子序列长度

        ans = 0 #用于记录最长公共子序列长度
        #递推公式 if nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1] + 1 ,如果i-1和j-1相等的话，那么其最长公共子序列长度至少为1，否则可能是0
        #如果他们共同后退一步之后（即dp[i-1][j-1]），的最长公共子序列长度不为零（即dp[i-1][j-1] != 0），那么，也就是说至少num1[i-2] == num2[j-2] and nums1[i-1] == nums2[j-1]
        # 此时最长公共子序列长度至少为2，依次类推

        for i in range(1,len(nums1) + 1): #这里的i必须取到n(nums1)，因为dp数组的含义是包含i-1，如果i只到了n(nums1) - 1,那么最后一个元素就取不到
            for j in range(1,len(nums2) + 1):
                if (nums1[i - 1] == nums2[j - 1]):
                    dp[j][i] = dp[j - 1][i - 1] + 1
                    if dp[j][i] > ans:
                        ans = dp[j][i]

        return ans



if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,4,5]
    nums2 = [4,5,1,2,3]
    print(s.findLength2(nums1,nums2))






