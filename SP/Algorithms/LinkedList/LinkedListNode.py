class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push_ll(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append_ll(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def reverse_ll(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def find_cycle(self):
        if not self.head:
            return False

        fast = self.head
        slow = self.head

        while fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def create_cycle(self, pos):
        if pos < 0 or not self.head:
            return  # Invalid position or empty list

        last = self.head
        end = None
        index = 0

        # Find the node at the specified position
        while last.next:
            if index == pos:
                end = last
            last = last.next
            index += 1

        # Make the last node point to the node at the specified position
        if end:
            last.next = end

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(2, 21):
        ll.append_ll(i)
    ll.print_ll()
    ll.push_ll(1)
    ll.push_ll(3)
    ll.print_ll()
    print(f"\n Is there a cycle in the list? {ll.find_cycle()}")
    ll.reverse_ll()
    ll.print_ll()
    ll.create_cycle(3)
    print(f"\n Is there a cycle in the list? {ll.find_cycle()}")

