/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// Iterative approach
// class Solution {
//     public ListNode reverseList(ListNode head) {
//         ListNode n1 = null;
//         ListNode n2 = head;
//         ListNode tmp = n2;
//         while (n2 != null) {
//           tmp = n2.next;  
//           n2.next = n1;
          
//           n1 = n2;
//           n2 = tmp;
//         }
//         return n1;
//     }
// }


// Recursive approach
class Solution {
    public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) return head;
        ListNode tmp = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return tmp;
    }
}