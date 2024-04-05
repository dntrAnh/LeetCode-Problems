class Solution 
{
    public String makeGood(String s) 
    {
        if (s.length() == 1) {
            return s;
        }

        char[] ch = s.toCharArray();
        int i = 0;
        for (int j = 0; j < ch.length; i++, j++) {
            ch[i] = ch[j];
            if (i > 0 && isPair(ch[i - 1], ch[i])) {
                i -= 2;
            }
        }
        return new String(ch, 0, i);
    }

    private boolean isPair(char a, char b) {
        return Math.abs(a - b) == 32;
    }
}
