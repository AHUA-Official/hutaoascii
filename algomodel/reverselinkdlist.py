# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None  # 初始化前一个节点为 None
    curr = head  # 当前节点从头节点开始

    while curr is not None:
        next_node = curr.next  # 暂存当前节点的下一个节点
        curr.next = prev       # 反转当前节点的 next 指针
        prev = curr            # 前一个节点更新为当前节点
        curr = next_node       # 当前节点更新为下一个节点


        next = curr.next
        curr =
        prev =
        curr
    return prev  # 返回新的头节点（即原来的尾节点）

# 辅助函数：创建链表
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# 辅助函数：打印链表
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# 测试
arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
print("Original linked list:")
print_linked_list(head)

# 反转链表
reversed_head = reverse_linked_list(head)
print("Reversed linked list:")
print_linked_list(reversed_head)

# 使用递归法反转链表
head = create_linked_list(arr)
print("Original linked list (for recursive method):")
print_linked_list(head)

