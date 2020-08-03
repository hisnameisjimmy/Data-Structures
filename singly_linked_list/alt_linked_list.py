class Node:
    def __init__(self, value=None, next=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next = next

    def __repr__(self):
        return f'Node({self.value})->{self.next}'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        # set this node's next reference to the passed in node
        self.next = new_next


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the linked list
        self.tail = None

    def __repr__(self):
        ll = []
        cur = self.head
        while cur.next != None:
            ll.append(cur)
            cur = cur.next

        return f'HEAD: {self.head}{[node for node in ll if node != self.head and node != self.tail]} Tail: {self.tail}'

    # O(1)
    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # we have access to the end of the list, so we can directly add new nodes to it
    # O(1)
    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # what if the list is empty?
        if not self.head and not self.tail:
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # set the current tail's next to the new node
            self.tail.set_next(new_node)
            # set self.tail to the new node
            self.tail = new_node

    # we already have access to the head of the linked list, so we can directly remove from it
    # O(1)
    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        #what if head and tail are same node?
        elif self.head == self.tail:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head and tail
            self.head = self.head.get_next()
            self.tail = self.tail.get_next()
            return value
        # what if it isn't empty?
        elif self.head:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value

    # iterate over our linked list and print out each value in it
    def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()

    def contains(self, value):
        cur = self.head
        while cur != None:
            if cur.value != value:
                cur = cur.next
            else:
                return cur.value
        if cur == None:
            return None

    def get_tail(self):
        if self.tail:
            return self.tail.value
        else:
            return None

    def get_head(self):
        if self.head:
            return self.head.value
        else:
            return None

    def get_max(self):
        cur = self.head
        max = 0
        while cur != None:
            if cur.value > max:
                max = cur.value
            cur = cur.next

        if max > 0:
            return max
        else:
            return None


# ll = LinkedList()
# print(ll)


# for i in range(5):
#     ll.add_to_tail(i)

# print(ll)

linked_list = LinkedList()

linked_list.add_to_tail(1)

linked_list.add_to_tail(2)

linked_list.add_to_tail(3)

linked_list.add_to_tail(4)

linked_list.add_to_tail(5)
print(f"{linked_list}\n")
