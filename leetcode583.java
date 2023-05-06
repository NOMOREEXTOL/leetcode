/**
 * leetcode583题 ,动态规划解法
 * 64.55,5.08 (%)
 *
 *
 */


class Solution {
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word2.length() + 1][word1.length() + 1];

        for (int i = 1 ; i <= word1.length() ; i++) {
            for (int j = 1; j <= word2.length(); j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[j][i] = dp[j - 1][i - 1] + 1;
                } else {
                    dp[j][i] = Math.max(dp[j-1][i],dp[j][i-1]);
                }
            }
        }

        return word1.length() + word2.length() - 2 * dp[word2.length()][word1.length()];

    }
}
