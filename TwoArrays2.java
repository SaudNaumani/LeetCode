import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> Set = new HashSet<>();
        List<Integer> Result = new ArrayList<>();
        for (int i : nums1)
            Set.add(i);
        for (int j : nums2) {
            if (Set.contains(j)){
                Result.add(j);
                Set.remove(j);
            }
        }
        int[] ResultArr = new int[Result.size()];
        int k = 0;
        for (int l : Result) {
            ResultArr[k++] = l;
        }
        return ResultArr;
    }
}
