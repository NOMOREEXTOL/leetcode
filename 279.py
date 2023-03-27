class Solution():
    def numSquares(self,n:int)->int:
        """力扣279题，动态规划，给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 ，verson1：2740ms，13.8MB"""
        #生成不大于n的完全平方数表
        coins = []
        for _ in range(1,10**4+1):
            if (_) ** 2 <= n:
                coins.append((_)**2)

        #问题转化成零钱兑换的最小硬币数问题了
        dp = [n+1 for __ in range(n+1)] #dp数组的含义是背包容量为j时，所需要的最小硬币数为dp[j]
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i],n+1):
                dp[j] = min(dp[j],dp[j-coins[i]]+1)

        return dp[n]

    def numSquares2(self,n):
        """看题解，对空间复杂度优化，不需要用数组来存放完全平方数，直接遍历就行了，version2：2632ms，13.7MB"""

        dp = [n+1 for __ in range(n+1)] #dp数组的含义是背包容量为j时，所需要的最小硬币数为dp[j]
        dp[0] = 0

        for i in range(1,n+1):
            for j in range(i*i,n+1):        #i*i就是完全平方数了
                dp[j] = min(dp[j],dp[j-i*i]+1)

        return dp[n]


    def numSquares3(self,n):
        """看题解，尝试用BFS求解此题，算法基本思想是，每次遍历小于当前层的完全平方数，当remain第一次等于0的时候就是最小步数
        version3:612ms,16.2MB
        """
        queue = [Node(n)]
        memory = set()    #这里记录一下走过的层次数，因为，只有在第一次遇到n的时候，步数才是最小的，从第二次开始，如果再遇到n，
        #它的层数肯定比第一次遇到n小，所以已经没有遍历的必要了
        memory.add(n)

        while queue:
            """
            宽搜树大概为：（以n==13为例）
                        13
                   /       |   \ 
                  12       9    4   #比如在这一层如果遍历了12，那么如果在下一层又遇到12就没必要再遍历了，因为这里求的是最小步数
                 / | \   /  | \
                11  8 3  8  5  0
            """
            vertex = queue.pop(0)
            edges = [vertex.value - i*i for i in range(int(vertex.value**0.5)+1)]
            for edge in edges:
                if edge == 0:
                    return vertex.step+1
                else:
                    if edge not in memory:
                        queue.append(Node(edge,vertex.step+1))
                        memory.add(edge)



class Node():
    def __init__(self,value,step = 0):
        self.value = value
        self.step = step
    def __str__(self):
        return "value = {},step = {}".format(self.value,self.step)


if __name__ == "__main__":
    s = Solution()
    n = 12
    print(s.numSquares3(n))
