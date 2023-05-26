import java.util.Vector;

/**
 * leetcode349:magnet:?xt=urn:btih:ABDE19EC807ECC63BA61FF22A714C63796863DC3
 */

public class leetcode349 {
    public static void main(String[] args) {
//        int[] nums1 = {1,2,2,1};
//        int[] nums2 = {2,2};
//        int[] ans = intersection2(nums1,nums2);
//        for (int i = 0; i < ans.length; i++) {
//            System.out.println(ans[i]);
//        }

        int[] nums1 = {3,2,2,1};
        int[] nums2 = {9,8,7};
        quickSort(nums1,0,nums1.length - 1);
        quickSort(nums2,0,nums2.length - 1);

        for (int i = 0; i < nums1.length; i++) {
            System.out.println(nums1[i]);
        }

        for (int i = 0; i < nums2.length; i++) {
            System.out.println(nums2[i]);
        }


    }


    // 思路：对两个数组进行排序，维护两个指针，若两个指针值不相等，那么小的那个不断移动
    // 直到两个指针值相等或者刚移动的指针值比另外一个大，此时再移动另外一个
    // 若两指针值相等了，那么就把元素插入到ans当中，然后两指针同时移动。
    // 2ms,41.2MB(93.88,97.35 %)
    public static int[] intersection(int[] nums1,int[] nums2) {
        // 首先要对两个数组进行排序
        quickSort(nums1,0,nums1.length -1);
        quickSort(nums2,0,nums2.length - 1);

        Vector<Integer> integers = new Vector<>();
        int left = 0,right = 0;

        while (left < nums1.length && right < nums2.length) {
            if (nums1[left] == nums2[right]) {
                integers.add(nums1[left]);
                left++;
                right++;
                while (left < nums1.length &&
                        nums1[left - 1] == nums1[left]) {
                    left++;
                }
                while (right < nums2.length &&
                        nums2[right - 1] == nums2[right]) {
                    right++;
                }
            } else if (nums1[left] < nums2[right]) {
                while (left < nums1.length &&
                    nums1[left] < nums2[right]) {
                        left++;
                }
            } else {
                while (right < nums2.length &&
                    nums2[right] < nums1[left]) {
                    right++;
                }
            }
        }

        Object[] ansMid = integers.toArray();
        int[] ans = new int[ansMid.length];
        for (int i = 0; i < ansMid.length; i++) {
            ans[i] = (int)ansMid[i];
        }
        return ans;

    }


    // 思路2：维护一个hash表（大小为1000），对于nums1为增长2，对于nums2为减小1
    // 最后为1的就是二者重复的
    // 1ms,41.1MB(98.6,98.57 % )
    public static int[] intersection2(int[] nums1,int[] nums2) {
        int[] hashList = new int[1001];

        for (int i : nums1) {
            if (hashList[i] == 0) {
                hashList[i] += 2; // 如果是0的话就加2
            }
        }

        for (int i : nums2) {
            if (hashList[i] == 2) {
                hashList[i] -= 1;
            }
        }

        Vector<Integer> ansMid = new Vector<Integer>();
        for (int i = 0; i < hashList.length; i++) {
            if (hashList[i] == 1) {
                ansMid.add(i);
            }
        }
        Object[] ansmid = ansMid.toArray();
        int[] ans = new int[ansmid.length];

        for (int i = 0; i < ansmid.length; i++) {
            ans[i] = (int)ansmid[i];
        }

        return ans;

    }


    public static void quickSort(int[] nums,int start,int end) {
        if (end <= start) {return;}

        int low = start;
        int high = end;

        int midValue = nums[low];

        while (low < high) {
            while (low < high && nums[high] >= midValue) {
                high--;
            }
            nums[low] = nums[high];
            while (low < high && nums[low] < midValue) {
                low++;
            }
            nums[high] = nums[low];
        }

        nums[low] = midValue;
        quickSort(nums,start,low - 1);
        quickSort(nums,low + 1,end);
    }

}
