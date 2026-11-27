class Node:
    """Represents one node in a singly linked list."""

    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None

    def create(self, values):
        """Create a linked list from a collection of values."""
        for value in values:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head

                # Move to the last node
                while current.next is not None:
                    current = current.next

                # Attach the new node at the end
                current.next = new_node

    def traverse(self):
        """Visit and print every node from head to end."""
        current = self.head

        if current is None:
            print("Linked list is empty")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")