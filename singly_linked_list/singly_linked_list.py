class Node:
    def __init__(self, value=None, node_next=None):
        self.value = value
        self.node_next = node_next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.node_next

    def set_next(self, new_next):
        self.node_next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_head = Node(value)
        if self.length == 0:
            # It is both the head and the tail
            self.head = new_head
            self.tail = new_head
        else:
            # set the current head to the next value
            new_head.set_next(self.head)
            self.head = new_head
        self.length += 1

    def add_to_tail(self, value):
        new_tail = Node(value, None)
        # Same as add_to_head, if there is no head or tail, it is both
        if self.length == 0:
            self.tail = new_tail
            self.head = new_tail
        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail
        self.length += 1

    def contains(self, value):
        if self.head == None:
            return None
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.get_next()
        return False
        
    def get_max(self):
        current_node = self.head
        high_score = 0
        if self.head == None:
            return None
        while current_node is not None:
            if current_node.value > high_score:
                high_score = current_node.value
            current_node = current_node.get_next()
        return high_score

    def remove_head(self):
        if self.head == None:
            return None
        # Remove head is to make the head's next the actual head, no need to do anything else
        if self.head.get_next() == None:
            removed = self.head.get_value()
            self.length -= 1
            self.head = None
            self.tail = None
            return removed
        else:
            removed = self.head.get_value()
            self.length -= 1
            self.head = self.head.get_next()
            return removed

    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(f'{cur_node.get_value()} -> {cur_node.get_next() if cur_node.get_next() == None else cur_node.get_next().get_value()}')
            cur_node = cur_node.get_next()


linked_list = LinkedList()

# Mixed
linked_list.add_to_head(1)
linked_list.add_to_tail(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
linked_list.add_to_tail(5)
linked_list.add_to_head(6)
linked_list.print_list()


# Add to head only
# linked_list.add_to_head(1)
# linked_list.add_to_head(2)
# linked_list.add_to_head(3)
# linked_list.add_to_head(4)
# linked_list.add_to_head(5)
# linked_list.add_to_head(6)
# linked_list.print_list()



# Test None Next
# linked_list.add_to_head(1)
# linked_list.add_to_head(2)
# linked_list.add_to_head(3)
# print(linked_list.tail.value)

# Test get max
# linked_list.add_to_tail(100)
# linked_list.add_to_tail(55)
# linked_list.add_to_tail(101)
# print(linked_list.get_max())

# Contains
# linked_list.add_to_tail(1)
# linked_list.add_to_tail(2)
# linked_list.add_to_tail(5)
# linked_list.add_to_tail(10)
# print(linked_list.contains(10))

# Remove Head
# linked_list.add_to_tail(10)
# linked_list.add_to_tail(20)
# print(linked_list.remove_head())
# print(linked_list.contains(10))
# linked_list.remove_head()
# print(linked_list.contains(20))

# print(linked_list.head.value)
# print(linked_list.head.get_next().value)
# print(linked_list.tail.value)

# print(linked_list.head.value)
# print(linked_list.tail.value)
# linked_list.add_to_tail(20)
# linked_list.add_to_head(30)
# print(linked_list.print_list())
# print(linked_list.length)
