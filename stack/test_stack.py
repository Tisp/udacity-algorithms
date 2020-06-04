import pytest
from stack.stack import Stack
from linked_list.linked_list import Element


class TestStack:

    def test_stack(self):
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)
        e4 = Element(4)

        stack = Stack(e1)

        stack.push(e2)
        stack.push(e3)
        assert stack.pop().value == 3
        assert stack.pop().value == 2
        assert stack.pop().value == 1
        assert stack.pop() == None
        stack.push(e4)
        assert stack.pop().value == 4
