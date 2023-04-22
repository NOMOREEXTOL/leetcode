/**
 * leetcode718,version:Java
 * 20ms,50MB
 */



public class leetcode718 {

    public static int findLength(int[] nums1, int[] nums2) {
        final int L1 = nums1.length;
        final int L2 = nums2.length;
        int[][] dp = new int[L1 + 1][L2 + 1];
        int ans = 0;


        for (int i = 1; i <= nums1.length ; i++ ) {
            for (int j = 1 ; j <= nums2.length ; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if (dp[i][j] > ans)
                        ans = dp[i][j];
                }
            }
        }

        return ans;
    }
}