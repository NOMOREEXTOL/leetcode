/**
 * 实际运行2ms,39.3MB
 */


class Solution {
    public int maxProfit(int k, int[] prices) {
        int dp[] = new int[2 * k + 1];
        for (int i = 1; i <= 2 * k; i+=2) {
            dp[i] = -prices[0];
        }
        
        for (int j = 1 ; j < prices.length ; ++j) {
            for (int m = 1 ; m <= 2 * k ; m++) {
                if (m % 2 == 1) {
                    dp[m] = Math.max(dp[m],dp[m-1] - prices[j]);
                } else {
                    dp[m] = Math.max(dp[m],dp[m-1] + prices[j]);
                }
            }

        }
        return dp[2 * k];
    }
}
