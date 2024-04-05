public class Solution 
{
    public String makeGood(String s) 
    {
        StringBuilder sb = new StringBuilder(s);
        int i = 0;

        while (i < sb.length() - 1) {
            if (Math.abs(sb.charAt(i) - sb.charAt(i + 1)) == 32) {
                sb.delete(i, i + 2);
                if (i > 0) {
                    i--;
                }
            } else {
                i++;
            }
        }
        return sb.toString();
    }
}
