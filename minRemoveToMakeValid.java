class Solution 
{
    public String minRemoveToMakeValid(String s) 
    {
        int left = 0, right = 0;
        Stack<Character> res = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char currChar = s.charAt(i);

            if (currChar == '(') {
                left++;
            }
            if (currChar == ')') {
                right++;
            }
            if (right > left) {
                right--;
                continue;
            }
            else {
                res.push(currChar);
            }
        }
        
        StringBuilder result = new StringBuilder();
        while (!res.isEmpty()) {
            char currChar = res.pop();
            if (left > right && currChar == '(') {
                left--;
            }
            else { 
                result.append(currChar);
            }
        }
        return result.reverse().toString();
    }
}
