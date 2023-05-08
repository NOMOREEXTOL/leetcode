/**
 * leetcode647题，尝试动态规划和双指针解法
 */


public class leetcode647 {
    public static void main(String[] args) {
        String s = "aaa";
        System.out.println(countSubstrings(s));
    }

//    // 动态规划解法 11ms,42.7MB (31.45,7.42%)
//    public static int countSubstrings(String s) {
//        boolean[][] dp = new boolean[s.length()][s.length()];
//
//        int ans = 0;
//
//        for (int i = s.length() - 1; i >= 0; i--) {
//            for (int j = i ; j < s.length(); j++) {
//                if (s.charAt(i) == s.charAt(j)) {
//                    if (j - i <= 1) {
//                        dp[i][j] = true;
//                        ans++;
//                    } else {
//                        dp[i][j] = dp[i + 1][j - 1];
//                        if (dp[i][j]) {
//                            ans++;
//                        }
//                    }
//                }
//            }
//        }
//        return ans;
//    }
    // 双指针解法 3ms,39.6MB(87.33,76.66 %)
    public static int countSubstrings(String s) {
        int ans = s.length();

        // 先计算长度大于等于2且长度为偶数的回文子串个数

        for (int i = 0; i < s.length() - 1 ; i++) {
            int l = i;
            int r = i + 1;
            while (l >= 0 && r < s.length()) {
                if (s.charAt(l) == s.charAt(r)) {
                    ans++;
                    l--;
                    r++;
                } else {break;}
            }
        }

        // 计算长度大于2 且长度为奇数的回文子串个数

        for (int center = 1; center < s.length() ; center++) {
            int l = center - 1;
            int r = center + 1;
            while (l >= 0 && r < s.length()) {
                if (s.charAt(l) == s.charAt(r)) {
                    ans++;
                    l--;
                    r++;
                } else {break;}
            }
        }
        return ans;
    }
}