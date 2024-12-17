class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
# 创建链表实例
linked_list = LinkedList()

# 添加元素
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 打印原始链表
current = linked_list.head
while current:
    print(current.data)
    current = current.next

# 翻转链表
linked_list.reverse()

# 打印翻转后的链表
current = linked_list.head
while current:
    print(current.data)
    current = current.next