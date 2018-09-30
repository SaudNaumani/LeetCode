import java.util.Arrays;

class Solution {


    public int searchInsert(int[] nums, int target) {
        int temp;

        Arrays.sort(nums);

        //loop through the array
        for (int i = 0; i < nums.length; i++) {
            //if the target is in the array
            if (nums[i] == target)
                //return index
                return i;
        }
        for (int j = 0; j < nums.length; j++) {
            if (target < nums[0])
                return 0;
            if (target > nums[nums.length-1])
                return nums.length;
            //if the target is in between these two numbers
            if (target > nums[j-1] && target < nums[j+1])
                return j;
        }
        return 1;
    }
}
