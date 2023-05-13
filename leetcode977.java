import java.util.ArrayList;
import java.util.Vector;

/**
 * leetcode977: 双指针解法 2ms,44.3MB
 */

public class leetcode977 {
    public static void main(String[] args) {
        int[] nums = {1};
        int[] ans = sortedSquares(nums);
        for (int i = 0; i < ans.length; i++) {
            System.out.println(ans[i]);
        }
    }

    public static int[] sortedSquares(int[] nums) {
        int divIndex = nums.length - 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= 0) {
                if (i - 1 >= 0 &&(nums[i] * nums[i] <= nums[i - 1] * nums[i - 1])){
                    divIndex = i;
                } else if (i - 1 < 0){
                    divIndex = i;
                } else {
                    divIndex = i - 1;
                }
                break;
            }
        }

        int [] newNums = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            newNums[i] = nums[i] * nums[i];
        }

        ArrayList ans = new ArrayList(newNums.length);
        ans.add(newNums[divIndex]);

        int left = divIndex - 1;
        int right = divIndex + 1;

        while (left >= 0 && right < newNums.length) {
            if (newNums[left] <= newNums[right]) {
                ans.add(newNums[left--]);
            } else {
                ans.add(newNums[right++]);
            }
        }

        if (left == -1) {
            while (right < newNums.length) {
                ans.add(newNums[right++]);
            }
        }

        if (right == newNums.length) {
            while (left >= 0) {
                ans.add(newNums[left--]);
            }
        }
        Object[] ans2 = ans.toArray();
        int[] ans3 = new int[newNums.length];

        for (int i = 0; i < newNums.length; i++) {
            ans3[i] = (int)ans2[i];
        }
        return ans3;
    }
}






