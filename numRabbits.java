// 784.
class Solution 
{
    public int numRabbits(int[] answers) 
    {
        HashMap<Integer, Integer> coloredRabbits = new HashMap<>();
        int rabbits = 0;
        for (int ans : answers) {
            if (ans == 0) {
                rabbits++;
            }
            else {
                if (coloredRabbits.containsKey(ans)) {
                    if (coloredRabbits.get(ans) <= ans) {
                        coloredRabbits.put(ans, coloredRabbits.get(ans) + 1);
                    }
                    else {
                        rabbits = rabbits + ans + 1;
                        coloredRabbits.put(ans, 1);
                    }
                }
                else {
                    rabbits = rabbits + ans + 1;
                    coloredRabbits.put(ans, 1);
                }
            }
        }
        return rabbits;
    }
}
