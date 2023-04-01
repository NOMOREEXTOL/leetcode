//leetcode300,最长严格递增子序列，可以不连续:84ms,40.9MB
public class Leetcode300 {
	public int main(int[] nums) {
		int dp[] = new int[nums.length];
		for (int i = 0; i < nums.length ; ++i) {
			dp[i] = 1;
		}
		int maxLength = dp[0];
		for (int i = 1; i < nums.length ; i++) {
			for (int j = 0; j < i ; j++) {
				if (nums[j] < nums[i]) {
					dp[i] = Math.max(dp[i],dp[j] + 1);
				}
			}
			if (dp[i] > maxLength) {maxLength = dp[i];}
		}
		return maxLength;
	}
}




