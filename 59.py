class Solution():
    def generateMatrix(self,n):
        """
        思路：暴力解法，先构造一个指定大小的二维数组，初始化为0，再依次往里添元素
        添加元素的下标变化为顺时针（右，下，左，上）（(0,1),(1,0),(0,-1),(-1,0)）
        步长变化（循环次数） 为 n,n-1,n-1,n-2,n-2,.......1,1
        时间复杂度为O(n2)
        12ms,13.1MB
        """

        ans = [[0 for _ in range(n)] for __ in range(n)]

        dirConPara = 0 # 用于控制现在处于哪一个方向
        dirList = [(0,1),(1,0),(0,-1),(-1,0)]
        accuPara = 1 # 用于记录现在要填充哪一个数

        baseX = 0
        baseY = -1
        for i in range(n):
            baseX += dirList[dirConPara][0]
            baseY += dirList[dirConPara][1]
            ans[baseX][baseY] = accuPara
            accuPara += 1

        dirConPara += 1

        cirConPara = n - 1
        while cirConPara:
            for i in range(cirConPara):
                baseX += dirList[dirConPara][0]
                baseY += dirList[dirConPara][1]
                ans[baseX][baseY] = accuPara
                accuPara += 1
            dirConPara = (dirConPara + 1) % 4

            for i in range(cirConPara):
                baseX += dirList[dirConPara][0]
                baseY += dirList[dirConPara][1]
                ans[baseX][baseY] = accuPara
                accuPara += 1
            dirConPara = (dirConPara + 1) % 4

            cirConPara -= 1

        return ans





















if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(2))

