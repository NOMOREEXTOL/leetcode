/**
 * Leetcode1143:
 * 39ms,49.3MB
 */


class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];

        int ans = 0;

        for (int i = 1 ; i < text1.length() + 1 ; i++) {
            for (int j = 1 ; j < text2.length() + 1; j++) {
                if (text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[j][i] = dp[j - 1][i - 1] + 1;
                } else {
                    dp[j][i] = Math.max(dp[j - 1][i],dp[j][i - 1]);
                }
                if (dp[j][i] > ans)
                    ans = dp[j][i];
            }
        }
        return ans;
    }
}