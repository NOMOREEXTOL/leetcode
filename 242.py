class Solution():
    def isAnagram(self,s,t):
        """leetcode242
        64ms,13.1MB
        暴力解法：维护两个计数的hash表
        """
        if len(s) != len(t):
            return False

        countS = dict()
        for i in s:
            if countS.get(i):
                countS[i] += 1
            else:
                countS[i] = 1

        countT = dict()
        for j in t:
            if countT.get(j):
                countT[j] += 1
            else:
                countT[j] = 1

        for key in countS:
            if not countT[key]:
                return False

            if countS[key] != countT[key]:
                return False

        return True


    def isAnagram2(self,s,t):
        """
        解法二：尝试用一个hash表和两次for循环解决问题
        思路为：遍历下标，对于s，每遇到一个字母则加一。对于t则减一
        36ms,15.3MB(60.2,6.53 %)
        """
        if len(s) != len(t):
            return False

        LetterDict = dict()

        for index in range(len(s)):
            # 先检查s的
            if not LetterDict.get(s[index]):
                LetterDict[s[index]] = 1
            else:
                LetterDict[s[index]] += 1

            # 再检查t的
            if not LetterDict.get(t[index]):
                LetterDict[t[index]] = -1
            else:
                LetterDict[t[index]] -= 1

        for value in LetterDict.values():
            if value != 0:
                return False

        return True


    def isAnagram3(self,s,t):
        """
        题解解法：由于小写字母均是有序的，因此只需要维护一个长度为26的数组即可
        32ms,15.3MB(75.99,6.21%)
        """
        if len(s) != len(t):
            return False


        letterList = [0] * 26

        for index in range(len(s)):
            letterList[ord(s[index]) - ord('a')] += 1
            letterList[ord(t[index]) - ord('a')] -= 1

        for i in letterList:
            if i != 0:
                return False

        return True













if __name__ == '__main__':
    S = Solution()
    s = "cat"
    t = "car"
    print(S.isAnagram2(s,t))

