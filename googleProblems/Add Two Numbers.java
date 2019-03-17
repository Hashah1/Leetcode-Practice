// Link to problem: https://leetcode.com/problems/add-two-numbers/submissions/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode iterate_l1 = l1;
        ListNode iterate_l2 = l2;
        int sum = 0;
        
        while (iterate_l1.next != null && iterate_l2.next != null)
        {
            calculateSum(sum, iterate_l1, iterate_l2);

            // Move the two iterators to the next node
            iterate_l1 = iterate_l1.next;
            iterate_l2 = iterate_l2.next;
        } 

        calculateSum(sum, iterate_l1, iterate_l2);

        // if l2 is longer, merge the remainder characters to l1
        if (iterate_l2.next != null)
        {
            iterate_l1.next = l2;
        }
        return l1;
    }

    // Helper function to check for offset of each sum
    boolean isOffset(int sum){
        if (sum > 9)
            return true;
        return false;
    }
    
    void calculateSum(int sum, ListNode iterate_l1, ListNode iterate_l2)
    {
        // Calculate the sum of current node
        sum = iterate_l1.val + iterate_l2.val;
        System.out.println("Sum is: " + iterate_l1.val + " + " + iterate_l2.val + " = " + sum);

        // Pass sum to check if it has offset
        if (isOffset(sum)) {
            // If there is an offset, add 1 to the
            // next node's value and add 0 to current
            if (iterate_l1.next != null && iterate_l2.next != null)
                 iterate_l1.next.val += 1;
            
            // Check to see if there isnt anything next, add a new node to the end
            else if (iterate_l1.next == null || iterate_l2.next == null) {
                ListNode new_node = new ListNode(1);
                iterate_l1.next = new_node;
                }
            iterate_l1.val = 0;
        }
        // Else, add the sum to l1's current node value
        else {
            iterate_l1.val = sum;
        }
    }
}