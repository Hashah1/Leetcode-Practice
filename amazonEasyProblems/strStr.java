class Solution {
    public int strStr(String haystack, String needle) {
        int index = 0, temp_index = 0, needle_index = 0;
        int needle_count = needle.length();

        if (needle.length() == 0) {
            return index;
        }
        else if (needle.length() <= haystack.length())
        {
            for (int i = 0; i < haystack.length(); i++) {
                while (needle_index != needle_count)
                {
                    if (needle.charAt(needle_index) == haystack.charAt(i))
                    {
                        temp_index = i;

                    }
                    else {
                        break;
                    }
                    needle_index++;
                }
            }
            return Math.abs((a - temp_index));
        }
        return index = -1;
    }
}