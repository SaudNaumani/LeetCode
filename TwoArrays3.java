import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> Set = new HashSet<>();
        Set<Integer> Intersection = new HashSet<>();
        for (int i : nums1)
            Set.add(i);
        for (int j : nums2) {
            if (Set.contains(j)){
                Intersection.add(j);
            }
        }
        int[] Result = new int[Intersection.size()];
        int k = 0;
        for (int l : Intersection) {
            Result[k++] = l;
        }
        return Result;
    }
}
