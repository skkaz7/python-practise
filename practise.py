# Dell questions

# Median Of Two Sorted Arrays

# def median(list_a, list_b):
#     merged = sorted(list_a + list_b)
#     if len(merged) % 2 != 0:
#         return merged[len(merged) // 2]
#     else:
#         return (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2
#
#
# if __name__ == "__main__":
#     arr = [1, 2]
#     brr = [1, 4]
#     a = [-5, 3, 6, 12, 15]
#     b = [-12, -10, -6, -3, 4, 10]
#     print("Median: ", median(a, b))


# Merge One Sorted Array Into Another

# def merge_two_arrays(arr1, arr2):
#     n = len(arr1)
#     new_arr2 = arr2[:n]
#     return sorted(arr1 + new_arr2)
#
#
# if __name__ == "__main__":
#     arr1 = [1, 3, 5]
#     arr2 = [2, 4, 6, 0, 0, 0]
#     print("Output array: ", merge_two_arrays(arr1, arr2))


# Trawersowanie po drzewie - depth-first search, DFS

# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
#
#     # def __str__(self):
#     #     return f"Node: {self.name}"
#     def __repr__(self):
#         return str(self.name)
#
#     @staticmethod
#     def search(start_node, name):
#         visited = []
#         stack = [start_node]
#         while stack:
#             node = stack.pop()
#             if node not in visited:
#                 visited.append(node)
#
#             if node.name == name:
#                 return visited
#
#             for child in node.children:
#                 stack.append(child)
#
#
# if __name__ == "__main__":
#     root = Node('Mieszko 1')
#     n1 = Node('Bolesław Chrobry')
#     root.children.append(n1)
#     n2 = Node('Mieszko II')
#     n1.children.append(n2)
#     n3 = Node('Kazimierz Odnowiciel')
#     n2.children.append(n3)
#
#     n4 = Node('Bolesław Śmiały')
#     n5 = Node('Władysław Herman')
#     n3.children = [n4, n5]
#
#     n6 = Node('Zbigniew')
#     n7 = Node('Bolesław Krzywousty')
#     n5.children = [n6, n7]
#     print(Node.search(root, 'Zbigniew'))
#
#     root2 = Node(7)
#     r1 = Node(3)
#     root2.children.append(r1)
#     r2 = Node(15)
#     root2.children.append(r2)
#     r3 = Node(9)
#     r4 = Node(20)
#     r2.children = [r3, r4]
#     print(Node.search(root2, 20))


# Stos / Stack

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def __str__(self):
#         return str(self.stack)
#
#     def push(self, item):
#         return self.stack.append(item)
#
#     def is_empty(self):
#         return len(self.stack) <= 0
#
#     def pop(self):
#         return None if self.is_empty() else self.stack.pop()
#
#     def peek(self):
#         return None if self.is_empty() else self.stack[len(self.stack) - 1]
#
#
# if __name__ == "__main__":
#     my_stack = Stack()
#     my_stack.push('first el')
#     my_stack.push('second el')
#     my_stack.push('third el')
#     my_stack.pop()
#     my_stack.pop()
#     my_stack.pop()
#     print(my_stack.peek())
#     print(my_stack)


# Binary search algorithm

# def binary_search_algorithm(num, num_list):
#     left = 0
#     right = len(num_list) - 1
#
#     while left <= right:
#         middle = (left + right) // 2
#         if num_list[middle] == num:
#             print(f"Number {num} is on the list.")
#             break
#         elif num_list[middle] < num:
#             left = middle + 1
#         else:
#             right = middle - 1
#     else:
#         print(f"Number {num} is not on the list.")
#
#
# if __name__ == "__main__":
#     l = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]
#     binary_search_algorithm(341, l)


# Bubble sort

# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#
# if __name__ == "__main__":
#     data = [-2, 45, 0, 11, -9]
#     bubble_sort(data)
#     print('Sorted Array in Ascending Order:')
#     print(data)


# Optimized Bubble sort

# def optimized_bubble_sort(array):
#     for i in range(len(array)):
#         swapped = False
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#                 swapped = True
#
#         if not swapped:
#             break
#
#
# if __name__ == "__main__":
#     data = [-2, 45, 0, 11, -9]
#     optimized_bubble_sort(data)
#     print('Sorted Array in Ascending Order:')
#     print(data)


# Queue - Kolejka

# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def __str__(self):
#         return str(self.queue)
#
#     def enqueue(self, item):
#         return None if self.is_full() else self.queue.append(item)
#
#     def is_empty(self):
#         return len(self.queue) < 1
#
#     def dequeue(self):
#         return None if self.is_empty() else self.queue.pop(0)
#
#     def is_full(self):
#         return len(self.queue) == 5
#
#     def peek(self):
#         return self.queue[0]
#
#
# if __name__ == '__main__':
#     q = Queue()
#     print(q.dequeue())
#     q.enqueue('first')
#     q.enqueue('second')
#     q.enqueue('third')
#     q.enqueue('fourth')
#     q.enqueue('fifth')
#     q.enqueue('sixth')
#     print(q.peek())
#     print(q)


# Deque - Double Ended Queue

# class Deque:
#     def __init__(self):
#         self.deque = []
#
#     def display(self):
#         print(self.deque)
#
#     def size(self):
#         print(len(self.deque))
#
#     def add_front(self, item):
#         return self.deque.append(item)
#
#     def add_rear(self, item):
#         return self.deque.insert(0, item)
#
#     def remove_front(self):
#         return self.deque.pop()
#
#     def remove_rear(self):
#         return self.deque.pop(0)
#
#
# if __name__ == '__main__':
#     d = Deque()
#     d.add_rear(1)
#     d.add_rear(2)
#     d.add_rear(3)
#     d.add_front(0)
#     d.display()
#     d.remove_front()
#     d.remove_rear()
#     d.display()

# Linked list basics - lista połączona podstawy

# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(str(temp.item), end=' ')
#             temp = temp.next
#
#
# if __name__ == '__main__':
#     linked_list = LinkedList()
#
#     linked_list.head = Node('first')
#     second = Node(2)
#     third = Node(3)
#
#     linked_list.head.next = second
#     second.next = third
#     linked_list.print_list()


# Linked list operations

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beginning(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def insert_at_end(self, new_data):
#         new_node = Node(new_data)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         last = self.head
#         while last.next:
#             last = last.next
#
#         last.next = new_node
#
#     @staticmethod
#     def insert_after(prev_node, new_data):
#         if prev_node is None:
#             print("The given previous node must be in Linked List.")
#             return
#
#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
#
#     def delete_node(self, position):
#         if self.head is None:
#             return
#
#
#
#     def print_list(self):
#         temp = self.head
#         while temp:
#             print(str(temp.data), end='->')
#             temp = temp.next
#
#
# if __name__ == '__main__':
#     llist = LinkedList()
#     llist.insert_at_beginning(1)
#     llist.insert_at_beginning(2)
#     llist.insert_at_beginning(3)
#     llist.insert_at_end(4)
#     llist.insert_after(llist.head, 5)
#     llist.print_list()


# Linked list

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#
#         temp.next = Node(data, None)
#
#     def insert_values(self, data_list):
#         # self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#     def remove_at(self, index):
#         if index < 0 or index >= self.get_length():
#             raise Exception('Invalid index')
#
#         if index == 0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         temp = self.head
#         while temp:
#             if count == index - 1:
#                 temp.next = temp.next.next
#                 break
#
#             count += 1
#             temp = temp.next
#
#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             raise Exception('Invalid index')
#
#         if index == 0:
#             self.insert_at_beginning(data)
#
#         count = 0
#         temp = self.head
#         while temp:
#             if count == index - 1:
#                 node = Node(data, temp.next)
#                 temp.next = node
#                 break
#
#             count += 1
#             temp = temp.next
#
#     def print(self):
#         if self.head is None:
#             print('Linked list is empty')
#             return
#         temp = self.head
#         while temp:
#             print(str(temp.data), end='->')
#             temp = temp.next
#
#     def get_length(self):
#         count = 0
#         temp = self.head
#         while temp:
#             count += 1
#             temp = temp.next
#
#         return count
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     # ll.insert_at_beginning(1)
#     # ll.insert_at_beginning(2)
#     # ll.insert_at_beginning(3)
#     # ll.insert_at_end(0)
#     # ll.insert_at_end(-1)
#     ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
#     ll.remove_at(2)
#     print(ll.get_length())
#     ll.insert_at(0, 'figs')
#     ll.insert_at(2, 'apple')
#     ll.print()


# Tree - general tree

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def __str__(self):
#         return self.data
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#
#         return level
#
#     def print_tree(self):
#         spaces = '   ' * self.get_level()
#         prefix = spaces + '|__' if self.parent else ''
#         print(prefix + self.data)
#
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#
# if __name__ == '__main__':
#     root = TreeNode("Electronics")
#
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))
#
#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))
#
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))
#
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#     root.print_tree()


# Binary Tree ---> Binary search tree - BST

# class BinarySearchTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __str__(self):
#         return str(self.data)
#
#     def add_child(self, data):
#         if data == self.data:
#             return
#
#         if data < self.data:
#             # add data in left subtree
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTreeNode(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTreeNode(data)
#
#     def in_order_traversal(self):
#         elements = []
#
#         # visit left tree
#         if self.left:
#             elements += self.left.in_order_traversal()
#
#         # visit base node
#         elements.append(self.data)
#
#         # visit right tree
#         if self.right:
#             elements += self.right.in_order_traversal()
#
#         return elements
#
#     def search(self, value):
#         if self.data == value:
#             return True
#
#         if value < self.data:
#             if self.left:
#                 return self.left.search(value)
#             else:
#                 return False
#
#         if value > self.data:
#             if self.right:
#                 return self.right.search(value)
#             else:
#                 return False
#
#     def find_min(self):
#         if self.left is None:
#             return self.data
#         else:
#             return self.left.find_min()
#
#     def find_max(self):
#         if self.right is None:
#             return self.data
#         else:
#             return self.right.find_max()
#
#     def delete(self, value):
#         if value < self.data:
#             if self.left:
#                 self.left = self.left.delete(value)
#         elif value > self.data:
#             if self.right:
#                 self.right = self.right.delete(value)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.left
#
#             min_val = self.right.find_min()
#             self.data = min_val
#             self.right = self.right.delete(min_val)
#
#         return self
#
#
# if __name__ == '__main__':
#     numbers = [17, 4, 1, 20, 9, 23, 18, 34]
#
#
#     def build_tree(elements):
#         root = BinarySearchTreeNode(elements[0])
#         for i in range(1, len(elements)):
#             root.add_child(elements[i])
#         return root
#
#
#     numbers_tree = build_tree(numbers)
#     print(numbers_tree.in_order_traversal())
#     print(numbers_tree.search(20))
#     print(numbers_tree.find_min())
#     print(numbers_tree.find_max())
#     numbers_tree.delete(20)
#     print(numbers_tree.in_order_traversal())


# Graph

# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start, end in self.edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
#
#         print('Graph dict: ', self.graph_dict)
#
#     def get_paths(self, start, end, path=[]):
#         path = path + [start]
#
#         if start == end:
#             return [path]
#
#         if start not in self.graph_dict.keys():
#             return []
#
#         paths = []
#
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     paths.append(p)
#
#         return paths
#
#     def get_shortest_path(self, start, end, path=[]):
#         path = path + [start]
#
#         if start == end:
#             return path
#
#         if start not in self.graph_dict.keys():
#             return None
#
#         shortest_path = None
#
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_shortest_path = self.get_shortest_path(node, end, path)
#                 if new_shortest_path:
#                     if shortest_path is None or len(new_shortest_path) < len(shortest_path):
#                         shortest_path = new_shortest_path
#
#         return shortest_path
#
#
# if __name__ == '__main__':
#     routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]
#
#     route_graph = Graph(routes)
#
#     departure = 'Mumbai'
#     arrival = 'New York'
#
#     print(f'Paths between {departure} and {arrival}: ', route_graph.get_paths(departure, arrival))
#
#     print(f'Shortest path between {departure} and {arrival}: ', route_graph.get_shortest_path(departure, arrival))


# Recursion example

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)


if __name__ == '__main__':
    print(find_sum(5))


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(6))
