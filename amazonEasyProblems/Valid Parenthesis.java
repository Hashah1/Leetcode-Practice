import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        // Convert the string to a character array
        char [] parenthesis_array = s.toCharArray();
        char parenthesis_1;
        boolean is_round_closed = is_curly_closed = is_square_closed = true;

        // To keep a tally for every parenthesis encountered
        int round_count = 0, curly_count = 0, square_count = 0;

        // Create a stack and load it all with values
        Stack<Character> my_stack = new Stack<Character>();
        for (int i = 0; i < parenthesis_array.length; i++)
        {
            my_stack.push(parenthesis_array[i]);
        }
        
        // Loop until stack is empty
        while (!my_stack.isEmpty())
        {
            // Get the last two elements in stack
            parenthesis_1 = my_stack.pop();

            if (!my_stack.isEmpty())
            {
                if (parenthesis_1 == '(' || parenthesis_1 == ')')
                    is_round_closed = !is_round_closed;
                else if (parenthesis_1 == '{' || parenthesis_1 == '}')
                    is_curly_closed = !is_curly_closed;
                else if (parenthesis_1 == '[' || parenthesis_1 == ']')
                    is_square_closed = !is_square_closed;
            }
            // Check to see which parenthesis has been
            // removed and accordingly increment the tally
            // if (parenthesis_1 == '(' || parenthesis_1 == ')')
            //     round_count++;
            // else if (parenthesis_1 == '{' || parenthesis_1 == '}')
            //     curly_count++;
            // else
            //     square_count++;
        }
        if (is_round_closed && is_curly_closed && is_square_closed)
        {
            return true;
        }
        // if ((round_count % 2 == 0) && (curly_count % 2 == 0) && (square_count % 2 == 0))
        //     return true;
        return false;
    }
}