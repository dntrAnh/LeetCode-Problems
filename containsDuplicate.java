class Solution 
{
    public boolean containsDuplicate(int[] nums) 
    {
        Arrays.sort(nums);
        boolean check = false;
        for (int i = 1; i < nums.length; i++) {
            if ( nums[i] == nums[i - 1] ) {
                check = true;
            }
        }
        return check;
    }
}
