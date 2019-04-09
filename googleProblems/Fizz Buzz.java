class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>();
        for (int i = 1; i <= n; i++) {
            // If multiple of 3
            if (!(i%5 == 0) && (i%3 == 0)) {
                res.add("Fizz");
            }
            else if ((i%5 == 0) && !(i%3 == 0)) {
                res.add("Buzz");
            }
            else if ( (i%5 == 0) && (i%3 == 0) ) {
                res.add("FizzBuzz");
            }
            else {
                // Append numeric value to list
                res.add(String.valueOf(i));
            }
        }
        return res;
    }
}