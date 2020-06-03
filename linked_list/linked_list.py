"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


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
        while current.next and position != current_position:
            before = current
            current = current.next
            current_position += 1
        new_element.next = current
        before.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        pass





## Test cases
# Set up some Elements

# Test get_position
# Should print 3


# Test insert
# ll.insert(e4,3)
# # Should print 4 now
# print(ll.get_position(3).value)
#
# # Test delete
# ll.delete(1)
# # Should print 2 now
# print(ll.get_position(1).value)
# # Should print 4 now
# print(ll.get_position(2).value)
# # Should print 3 now
# print(ll.get_position(3).value)
