/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
function isDuplicates (arr) {
  const map = {}
  return arr.some((item, i) => {
      if (map[item]) {
          return true
      }
      map[item] = true
  })
}
/**
 * Решение с помощью O(3n)
* @param {ListNode} head
* @return {boolean}
*/
var isPalindrome = function(head) {
  // Решение с помощью 0(3n)
  const values = []
  while (head !== null) {
      values.push(head.val)
      head = head.next
  }
  const reversed = [...values].reverse()
  
  if (values.length === 1) return true
  // Если есть повторяющиеся
  if (isDuplicates(values)) {
      // Если массив = перевернутый массив
      return values.every((item, i) => item === reversed[i])    
  }
  return false
};