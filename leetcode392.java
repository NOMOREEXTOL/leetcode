/**
 * leetcode392,动态规划解法
 * 6ms,14.4MB
 */

//class Solution {
//    public boolean isSubsequence(String s, String t) {
//        int[][] dp = new int[s.length() + 1][t.length() + 1];
//
//        for (int i = 1; i <= s.length() ; i++) {
//            for (int j = 1; j <= t.length() ; j++) {
//                if (s.charAt(i - 1) == t.charAt(j - 1)) {
//                    dp[i][j] = dp[i-1][j-1] + 1;
//                } else {
//                    dp[i][j] = dp[i][j - 1];
//                }
//            }
//        }
//        return dp[s.length()][t.length()] == s.length();
//
//
//    }
//}


    //解法二 1ms,39.7MB
class Solution {
    public boolean isSubsequence(String s, String t) {
        int l = 0,r = 0;
        while (true) {
            if (l == s.length())
                return true;
            if (r == t.length())
                return false;
            while (r < t.length()) {
                if (l < s.length() && s.charAt(l) == t.charAt(r)) {
                    l++;
                    r++;
                } else {
                    r++;
                }
            }

        }



    }
}