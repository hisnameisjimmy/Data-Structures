class Node:
    # node characteristics
    # 1) has a value
    # 2) knows what is next in line
    # 3) knows what is previous in line
    # 4) can adjust next and previous, can get next and previous, can get value
    def __init__(self, value=None, next=None, previous=None)
        self.value = value
        self.next = next
        self.prev = prev

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new
    
    def get_previous(self):
        return self.prev

    def set_prev(self, new):
        self.prev = new

class LinkedList:
    # characteristics of linkedlist
    # 1) knows head, tail, and length
    # 2) Can set the head and tail
    # 3) Can delete a node??
    # 4) Can it reverse itself?
    # 5) Get max value
    # 6) Contains a value
    # 7) Remove head

    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.length = length

    def 
