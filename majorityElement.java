class Solution {
    public int majorityElement(int[] nums) 
    {
        int value = MajorityElement(nums, nums[0], 0);
        return value;
    }

    public int MajorityElement(int[] nums, int val, int index) 
    {
        int count = 0;
        for (int i = index; i < nums.length; i++) {
            if (nums[i] == val) {
                count++;
            } 
            else {
                count--;
            }

            if (count < 0) {
                return MajorityElement(nums, nums[i], i);
            }
        }
        return val;
    }
}
