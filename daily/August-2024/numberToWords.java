public class Solution {
    private final String[] single = new String[] { "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine" };
    private final String[] teens = new String[] { "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen" };
    private final String[] tens = new String[] { "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety" };

    public String numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }
        return findNum(num);
    }

    private String findNum(int num) {
        StringBuilder result = new StringBuilder();

        if (num < 10) {
            result.append(single[num]);
        }

        else if (num < 20) {
            result.append(teens[num - 10]);
        }

        else if (num < 100) {
            result.append(tens[num / 10]);
            int remainder = num % 10;
            if (remainder > 0) {
                result.append(" ").append(single[remainder]);
            }
        }

        else if (num < 1000) {
            result.append(single[num / 100]).append(" Hundred");
            int remainder = num % 100;
            if (remainder > 0) {
                result.append(" ").append(findNum(remainder));
            }
        }

        else if (num < 1000000) {
            result.append(findNum(num / 1000)).append(" Thousand");
            int remainder = num % 1000;
            if (remainder > 0) {
                result.append(" ").append(findNum(remainder));
            }
        }

        else if (num < 1000000000) {
            result.append(findNum(num / 1000000)).append(" Million");
            int remainder = num % 1000000;
            if (remainder > 0) {
                result.append(" ").append(findNum(remainder));
            }
        }

        else {
            result.append(findNum(num / 1000000000)).append(" Billion");
            int remainder = num % 1000000000;
            if (remainder > 0) {
                result.append(" ").append(findNum(remainder));
            }
        }
        return result.toString().trim();
    }
}
