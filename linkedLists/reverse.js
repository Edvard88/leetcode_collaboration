/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  let prev = null
  let curr = head
  while(curr !== null) {
      let nextTemp = curr.next // Сохраняем ссылку на следующую ноду
      curr.next = prev // у текущего ставим ссылку на предыдущий
      prev = curr // записываем текущий в предыдущий
      curr = nextTemp // в текущий записываем следующий
  }
  return prev
}