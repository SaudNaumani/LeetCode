class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            if (nums[start] < nums[end])
                return nums[start];
            int mid = (start + end)/2;

            if (nums[start] <= nums[mid]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return nums[start];
    }
}

// Compare first and last element
    // If first is less than last; no rotation happened
        // Return first element as minimum
// Compute middle element and compare with first
    // If first is less than middle, we know that the rotation is in the other half
    // else it is in the first half of the array
