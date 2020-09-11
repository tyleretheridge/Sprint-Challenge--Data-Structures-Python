class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Need a case for empty list
        if not node:
            # Can't reverse empty list
            return
        # If at tail
        if not node.next_node:
            # Set tail to head
            self.head = node
            # Set prev ref to next
            node.set_next(prev)
            return
        # Recursion
        # Successive nodes in recursion will become prevs
        # Save node.next_node to node_prime before updating node.next_node
        node_prime = node.get_next()
        # Update node.next_node = prev input
        node.set_next(prev)
        # Recursive function call
        return self.reverse_list(node_prime, node)
