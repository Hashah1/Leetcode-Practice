// Definition for singly-linked list.
// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode(int x) { val = x; }
// }
INCOMPLETE
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Create a node pointing to the head of l1
        ListNode iterate = l1;

        // Loop iterater to the tail of l1
        while(iterate.next != null)
        {
            iterate = iterate.next;
        }
        // Merge the list
        iterate.next = l2; 
        sort(l1);

        ListNode a = l1;
        while(a != null)
        {
            System.out.println(a.val);
            a = a.next;
        }

        return l1;
    }

    // This function sorts the entire list in ascending order
    public void sort(ListNode l1)
    {
        ListNode slow = l1;
        ListNode fast = l1.next;
        int temp;

        while (fast != slow){
            if (fast.val <= slow.val) {
                // Swap values
                temp = fast.val;
                fast.val = slow.val;
                slow.val = temp;
            }                
                slow = slow.next;
                if (fast.next != null)
                    fast = fast.next;
        }

    }
}