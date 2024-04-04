class Solution 
{
    public int maxDepth (String s) 
    {
        Stack<String> parens = new Stack<>();
        int max = 0;
        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                parens.push("(");
            }
            if (parens.size() > max) {
                max = parens.size();
            }
            else if(s.charAt(i) == ')')
                parens.pop();
        }
        return max;
    }
}
