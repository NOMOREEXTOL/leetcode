//leetcode309题,version1:1ms,39.8MB
//version2:0ms,39.5MB
public class Leetcode309 {
	public int maxProfit(int[] prices) {
		//Version1
		// int dp[][] = new int[prices.length][4];//dp[0]持有，dp[1]未持有,dp[2]当天卖，dp[3]冷冻期
		// dp[0][0] = -prices[0];

		// for (int i = 1; i < prices.length ; ++i) {
		// 	dp[i][0] = Math.max(Math.max(dp[i-1][0],dp[i-1][1] - prices[i]),
		// 		       Math.max(dp[i-1][0],dp[i-1][3] - prices[i]));
		// 	dp[i][1] = Math.max(dp[i-1][1],dp[i-1][3]);
		// 	dp[i][2] = dp[i-1][0] + prices[i];
		// 	dp[i][3] = dp[i-1][2];
		// }
		// return Math.max(Math.max(dp[prices.length-1][1],
		// 				         dp[prices.length-1][2]),
		//                 Math.max(dp[prices.length-1][1],
		//                 	     dp[prices.length-1][3]));
		//Version2
		int dp[] = {0,0,0,0};
		dp[0] = -prices[0];

		for (int i = 1; i < prices.length ; i++) {
			int temp = 0;
			dp[0] = Math.max(Math.max(dp[0],dp[1]-prices[i]),Math.max(dp[0],dp[3] - prices[i]));
			dp[1] = Math.max(dp[1],dp[3]);
			dp[3] = dp[2];
			dp[2] = dp[0] + prices[i];
		}
		return Math.max(Math.max(dp[1],dp[2]),Math.max(dp[2],dp[3]));
	}
}