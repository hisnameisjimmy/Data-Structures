"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new

    def get_prev(self):
        return self.prev

    def set_prev(self, new):
        self.prev = new

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # Prev and next are none when there's only a single node
    # 
    def add_to_head(self, value):
        new_head = ListNode(value)
        if self.length == 0:
            self.head = new_head
            self.tail = new_head
        else:
            # I need to set the new_head to be prev to the old head
            # And the old head is now the next of the new head
            new_head.set_next(self.head)
            self.head.set_prev(new_head)
            self.head = new_head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # removed = self.head
        # if self.length == 1:
        #     self.head = None
        #     self.length = 0
        #     self.tail = None
        # else:
        #     # self.head.next is the new head
        #     self.head = get_next(self.head)
        # return removed
        removed = self.head.value
        next_to_head = self.head.next
        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
        else:
            next_to_head.set_prev(None)
            self.head = next_to_head
        return removed
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value)
        if self.length == 0:
            self.head = new_tail
            self.tail = new_tail
        else:
            # I need to set the new_head to be prev to the old head
            # And the old head is now the next of the new head
            new_tail.set_prev(self.tail)
            self.tail.set_next(new_tail)
            self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        removed = self.tail.value
        previous_to_tail = self.tail.prev
        if self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
        else:
            previous_to_tail.set_next(None)
            self.tail = previous_to_tail
        return removed
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # Make the current node's previous and next items related to eachother instead of the node itself
        # update the current tail's next to the new node
        # set current node prev to the current tail
        # set the current node equal to the tail
        self.delete(node)
        self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        elif node == self.tail:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            node.get_prev().set_next(node.get_next())
            node.get_next().set_prev(node.get_prev())
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
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

    def print_list_next(self):
        cur_node = self.head
        while cur_node is not None:
            print(f'{cur_node.get_value()} -> {cur_node.get_next() if cur_node.get_next() == None else cur_node.get_next().get_value()}')
            cur_node = cur_node.get_next()

    def print_list_prev(self):
        cur_node = self.tail
        while cur_node is not None:
            print(f'{cur_node.get_value()} <- {cur_node.get_prev() if cur_node.get_prev() == None else cur_node.get_prev().get_value()}')
            cur_node = cur_node.get_prev()


linked_list = DoublyLinkedList()

# Mixed
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
linked_list.add_to_head(5)
linked_list.remove_from_tail()

linked_list.print_list_next()
linked_list.print_list_prev()
