"""动态规划与递归的过程正好是相反的，动态规划是由基态逐渐过渡到指定规模
而递归则是从大问题逐步分解成小问题。rob1深搜超时的原因是，第一种情况考虑了父节点的子节点，
第二种情况考虑了父结点子节点的各子节点，这是存在重复计算的，第一种情况遍历完，实际上第二种情况的结果也出来了。
故可以采用记忆化递归进行优化。即先计算孙子节点，然后再结算左右子节点的时候就可以复用孙子节点的结果了。
"""


class Queue():
    def __init__(self,elems = []):
        self.elems = list(elems)

    def enqueue(self,items):
        self.elems.append(items)

    def dequeue(self):
        return self.elems.pop(0)

    def is_empty(self):return not self.elems

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinTree():
    def __init__(self,root = None):
        self.root = root

    def widthOrder(self):
        """定义二叉树的宽度优先遍历,返回一个宽度优先遍历的列表"""
        qu = Queue()
        cur = self.root
        qu.enqueue(cur)
        ans = []

        while not qu.is_empty():
            cur = qu.dequeue()
            if cur is None:
                ans.append(None)
                continue
            ans.append(cur.val)
            qu.enqueue(cur.left)
            qu.enqueue(cur.right)
        return ans

class Solution():
    def rob(self,root):
        """打家劫舍三,数据组织形式为二叉树,采用深搜递归超时。"""
        #递推公式为dp[i] = max(dp[2*i+1]+dp[2*i+2],cur.value + dp[4*i+3] + dp[4*i+4] + dp[4*i+5] + dp[4*i+6]) 即分为取本层的和不取本层的
        #则初始化就把所有的叶节点初始化，如果是NULL就是0，从叶节点向根节点迭代

        def Recursion(cur):
            if cur is None:
                return 0
            #取本层的
            if cur.left is not None:
                LL = Recursion(cur.left.left)
                LR = Recursion(cur.left.right)
                L = Recursion(cur.left)
            else:
                LL = 0
                LR = 0
                L = 0
            if cur.right is not None:
                RL = Recursion(cur.right.left)
                RR = Recursion(cur.right.right)
                R = Recursion(cur.right)
            else:
                RL = 0
                RR = 0
                R = 0
            midNum1 = L + R
            midNUm2 = cur.val + LL + LR + RL + RR
            return max(midNUm2,midNum1)

        return Recursion(root)


    def rob2(self,root):
        """采用深搜超时，现在考虑将传入的二叉树进行宽度优先遍历，然后对遍历列表进行处理"""
        widthList = BinTree(root).widthOrder() #宽搜之后加上None,数组为完全二叉树
        n = len(widthList)
        g = lambda x : x if x is not None else 0
        for node in range(len(widthList)//2,-1,-1):  #从n//2往后的节点均为叶节点
            if 2*node+2 < n:
                L = g(widthList[2*node + 1])
                R = g(widthList[2*node + 2])
            else:
                L = 0
                R = 0
            if 4*node + 6 < n:
                LL = g(widthList[4 * node + 3])
                LR = g(widthList[4 * node + 4])
                RL = g(widthList[4 * node + 5])
                RR = g(widthList[4 * node + 6])
            else:
                LL = 0
                LR = 0
                RL = 0
                RR = 0
            widthList[node] = max(L+R,g(widthList[node]) + LR + LL + RR + RL)
        return widthList[0]


    def rob3(self,root):
        """题解，树形结构动态规划入门题,24ms,16.8MB"""
        dp = [0,0] #dp数组的含义为dp[0]表示不取当前节点，所得到的最大价值，dp[1]表示取当前节点所得到的最大值

        def Recursion(cur):
            if cur is None:
                return [0,0] #当前节点为None时，返回取与不取当前节点，得到的最大价值都是0
            #由于需要知道子节点的状态来推导当前节点的最大值，所以二叉树的遍历采用后序遍历
            leftdp = Recursion(cur.left)
            rightdp = Recursion(cur.right)

            #对于本层，有两种状态
            val1 = cur.val + leftdp[0] + rightdp[0] #表示取当前节点，那么既然取了当前节点，那么其子节点就不能再取了
            #所以这里后面加的是对应子节点的0号位
            val2 = max(leftdp[0],leftdp[1])+ max(rightdp[0],rightdp[1]) #不取当前节点，不代表就一定要取其子节点
            #所以这里应该是取与不取各子节点所得到的最大价值的和
            return [val2,val1]

        return max(Recursion(root)) #返回取与不取根节点的最大值


    def rob4(self,root):
        """记忆化递归解法,36ms,17.8MB"""
        memoryDict = {} #memory字典记录的是以每一个节点为父结点，往下偷所能获得的最大价值
        def Recursion(cur):
            if cur is None:
                return 0
            if memoryDict.get(cur) is not None: #如果从当前节点往下偷的最大值已经算过一遍了，那直接返回就行了
                return memoryDict[cur]
            #取当前节点的情况，那么最大价值就是当前节点的价值加上考虑孙子节点的最大值
            #如果本轮当中，各孙子节点没有被计算过，那么就会计算，然后将计算结果存入memoryDict当中
            #这样，当第二种情况求考虑子节点的最大值时，就可以直接用memoryDict里面的数据了，不用重复遍历
            val1 = cur.val
            if cur.left:
                val1 += Recursion(cur.left.left) + Recursion(cur.left.right)
            if cur.right:
                val1 += Recursion(cur.right.left) + Recursion(cur.right.right)

            #不取当前节点
            val2 = Recursion(cur.left) + Recursion(cur.right)

            memoryDict[cur] = max(val2,val1)
            return memoryDict[cur]
        return Recursion(root)


if __name__ == "__main__":
    s = Solution()
    node  = Node(2,None,Node(3,None,Node(1)))
    print(s.rob4(node))