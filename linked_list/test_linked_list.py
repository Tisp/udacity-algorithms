import pytest
from linked_list.linked_list import LinkedList, Element


class TestLinkedList:

    def setup(self):
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)

        self.ll = LinkedList(e1)
        self.ll.append(e2)
        self.ll.append(e3)

    def test_get_position(self):
        assert self.ll.head.next.next.value == 3
        assert self.ll.get_position(3).value == 3
        assert self.ll.get_position(1).value == 1
        assert self.ll.get_position(2).value == 2

    def test_insert_position(self):
        e4 = Element(4)
        e5 = Element(5)
        self.ll.insert(e4, 3)
        assert self.ll.get_position(3).value == 4
        self.ll.insert(e5, 3)
        assert self.ll.get_position(3).value == 5
        assert self.ll.get_position(4).value == 4

    def test_delete_position(self):
        self.ll.delete(1)
        assert self.ll.get_position(1).value == 2
        assert self.ll.get_position(2).value == 3
        assert self.ll.get_position(3).value == 3
