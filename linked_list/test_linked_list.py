import pytest
from linked_list.linked_list import LinkedList, Element


class TestLinkedList:

    def setup(self):
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)
        e4 = Element(4)

        self.ll = LinkedList(e1)
        self.ll.append(e2)
        self.ll.append(e3)

    def test_get_position(self):
        assert self.ll.head.next.next.value == 3
        assert self.ll.get_position(3).value == 3
        assert self.ll.get_position(1).value == 1
