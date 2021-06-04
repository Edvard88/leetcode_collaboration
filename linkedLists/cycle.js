/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
// Решение с помощью проверки узлов на посещение
// var hasCycle = function(head) {
  
//   if (!head || !head.next) return false
  
//   const visited = [];
//   while (head !== null) {
//     if (visited.includes(head.next)) {
//       return true
//     }
//     visited.push(head.next);
//     head = head.next;
//   }
//   return false
// };

// Решение с помощью Алгоритма Флойда
var hasCycle = function(head) {
  let slow = head
  let fast = head
  while(fast !== null && fast.next !== null) {
    slow = slow.next
    fast = fast.next.next
    if (slow === fast) {
      return true
    }
  }
  return false
}