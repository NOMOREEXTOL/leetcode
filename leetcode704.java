/**
 * leetcode704:二分查找算法
 *  0ms,43.8MB(100,5.02%)
 *
 */
public class leetcode704 {
    public static void main(String[] args) {

    }

    public static int search(int[] nums,int target) {
        binsearch(nums,target,0,nums.length - 1);
    }

    public static int binsearch(int[] nums,int target,int start,int end) {
        if (end - start == 1) {
            if (nums[end] == target) {
                return end;
            }
            if (nums[start] == target) {
                return start;
            }
            return -1;
        }

        int l = start;
        int r = end;
        int mid = (l + r) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            return binsearch(nums,target,l,mid - 1);
        } else {
            return binsearch(nums,target,mid + 1,r);
        }
    }
}


