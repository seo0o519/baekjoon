import sys
data = list(map(int, sys.stdin.readline().split()))
ans_lst = []
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None
    def is_empty(self):
        return self.tail is None

    def add_tail(self, node_new):
        if self.is_empty():
            self.tail = node_new
            self.tail.next = node_new
        else:
            node_new.next = self.tail.next
            self.tail.next = node_new
            self.tail = node_new
    def remove_next_node(self, current_node):
        current_node.next = (current_node.next).next
lst = CircularLinkedList()
for i in range(data[0]):
    lst.add_tail(Node(i+1))

current_node = lst.tail
for k in range(data[0]):
    for i in range(data[1]-1):
        current_node = current_node.next
    ans_lst.append(current_node.next.item)
    lst.remove_next_node(current_node)

formatted_str = "<{}>".format(", ".join(map(str, ans_lst)))
print(formatted_str)