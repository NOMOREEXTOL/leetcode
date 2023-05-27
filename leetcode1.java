import org.omg.PortableInterceptor.INACTIVE;

import java.util.Collection;
import java.util.HashMap;


/**
 * leetcode1:两数之和
 */

public class leetcode1 {
    public static void main(String[] args) {

    }


    // 思路，构造一个hash表记录每一项的下标值，对原数组进行排序，采用双指针依次移动右指针直到等于目标值
    // 这个思路会人为的将所有元素入表，这样当遇到重复元素的时候会把前一个元素覆盖而造成错误。
    public static int[] twoSum(int [] nums, int target) {
        HashMap<String, Integer> hashList = new HashMap();
        // 将数组元素下标写入hash表

        for (int i = 0; i < nums.length; i++) {
            String s = nums[i] + "";
            hashList.put(s,i);
        }

        quickSort(nums,0,nums.length - 1);

        int left = 0,right = nums.length - 1;
        int[] ans = new int[2];
        int currentSum;

        while (left < right) {
            currentSum = nums[left] + nums[right];
            if (currentSum == target) {
                ans[0] = hashList.get(nums[left] + "");
                ans[1] = hashList.get(nums[right] + "");
                return ans;
            } else {right--;}
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

    // 思路：边遍历，边把遍历过的元素如hash表，这样在判断当前元素时就可以判断之前有没有所需要的元素了
    // 这里不用担心重复的问题，因为比如3 3 合成6，那么若此时这种情况是答案的话，情况必定是一个在hash表内，另一个3就是正在遍历的当前元素
    // 1ms,42.8MB(98.32,7.20 %)
    public static int[] twoSum2(int[] nums, int target) {
        HashMap<Integer, Integer> hM = new HashMap<>();

        int[] ans = new int[2];
        hM.put(nums[0],0);
        int needValue;

        for (int i = 1; i < nums.length; i++) {
            needValue = target - nums[i];
            if (hM.containsKey(needValue)) { // 如果所需要的值遍历过了，那么就直接输出
                ans[0] = i;
                ans[1] = hM.get(needValue);
                return ans;
            } else { // 否则就把当前遍历元素加入hash表,这个过程会更新重复元素的下标，但答案只要求一个，所以更新了也问题不大
                hM.put(nums[i],i);
            }
        }
        return ans;
    }

}

