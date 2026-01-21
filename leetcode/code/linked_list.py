#链表结构
class ListNode:
    """链表节点类"""
    def _init_(self,val : int):
        self.val = val
        self.next:ListNode|None = None #python中可以随时随地给对象赋新的属性

#访问节点
def access(head: ListNode, index: int) -> ListNode | None:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if head.next == None:
            return None
        head = head.next
    return head

#查找节点
def find(head: ListNode, target: int) -> int:
    """在链表中查找值为 target 的首个节点"""
    while head: #只要head的值不是None就一直循环
        index = 0
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1