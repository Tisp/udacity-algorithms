class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        current_position = 1
        while current.next and position != current_position:
            current = current.next
            current_position += 1
        return current

    def insert(self, new_element, position):
        current = self.head
        before = current
        current_position = 1

        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        while current.next and position != current_position:
            before = current
            current = current.next
            current_position += 1
        new_element.next = current
        before.next = new_element

    def delete(self, value):
        current = self.head
        before = current

        if self.head.value == value:
            self.head = self.head.next
            return

        while current.next and current.value != value:
            before = current
            current = current.next
        before.next = current.next
