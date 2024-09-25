class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to add new nodes at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    # Function to print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    # Function to merge two sorted linked lists
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        
        return result
    
    # Function to split the linked list into two halves
    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Function to perform merge sort on the linked list
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        # Get the middle of the list
        middle = self.get_middle(head)
        next_to_middle = middle.next
        
        # Split the list into two halves
        middle.next = None
        
        # Apply merge_sort on both halves
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        
        # Merge the sorted halves
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
    
    # Function to start the merge sort process
    def sort(self):
        self.head = self.merge_sort(self.head)

# Driver code to test the sorting of a linked list
if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()
    
    # Adding elements 3, 4, 1, 2 to the linked list
    llist.append(3)
    llist.append(4)
    llist.append(1)
    llist.append(2)
    
    print("Original Linked List:")
    llist.print_list()
    
    # Sort the linked list
    llist.sort()
    
    print("Sorted Linked List:")
    llist.print_list()
