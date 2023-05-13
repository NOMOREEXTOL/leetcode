/**
 * leetcode209: 1ms,52.7MB (100,5.04 %)
 */

public class leetcode209 {
    public static void main(String[] args) {
        int[] target = {};
        int sum = 4;
        int ans = minSubarrayLens(target,sum);
        System.out.println(ans);


    }

    public static int minSubarrayLens(int[] nums,int target) {
        if (nums.length == 0 || nums == null || target == 0) {
            return 0;
        }

        int temp = 0;
        for (int i = 0; i < nums.length; i++) {
            temp += nums[i];
            if (temp > target) {break;}
        }
        if (temp < target) {
            return 0;
        }

        int slow = 0;
        int minLens = nums.length;
        int curSum = nums[0];
        int fast;

        for (fast = 1; fast < nums.length; ) {
            if (curSum < target) {
                curSum += nums[fast++];
            } else { // 区间总和首次大于target，则更新最小区间长度
                while (slow <= fast && curSum >= target) {
                    if (fast - slow < minLens) {
                        minLens = fast - slow;
                    }
                    curSum -= nums[slow++];
                }
            }
        }

        while (slow <= fast && curSum >= target) {
            if (fast - slow < minLens) {
                minLens = fast - slow;
            }
            curSum -= nums[slow++];
        }

        return minLens;

    }

}