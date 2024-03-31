class Solution 
{
    public long countSubarrays(int[] nums, int minK, int maxK) 
    {
        long numSubArr = 0;
        int lastOcurr = -1;
        int leftIdx = -1;
        int rightIdx = -1;

        for (int i = 0; i < nums.length; ++i) {
            if (!(minK <= nums[i] && nums[i] <= maxK)) {
                lastOcurr = i;
            }

            if (nums[i] == minK) {
                leftIdx = i;
            }

            if (nums[i] == maxK) {
                rightIdx = i;
            }

            numSubArr = numSubArr + Math.max(0, Math.min(leftIdx, rightIdx) - lastOcurr);
        }

        return numSubArr;
    }
}
