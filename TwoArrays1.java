import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> Set = new HashSet<>();

        for (int i : nums1) {
            for (int j : nums2) {
                if (i == j)
                    Set.add(i);
            }
        }
        int[] Result = new int[Set.size()];
        int k = 0;
        for (int l : Set) {
            Result[k++] = l;
        }
        return Result;
    }
}
