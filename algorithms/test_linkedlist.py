import pytest
from linkedlist import Node, LinkedList  # add exact path later

class TestLinkedList:

    def test_add_first(linkedlist):
        
        assert LinkedList.add_first()

    def test_add_last(linkedlist):
        assert LinkedList.add_last()

    def test_add_before(linkedlist):
        assert LinkedList.add_before
    
    def test_add_after(linkedlist):
        assert LinkedList.add_after

    def test_remove(linkedlist):
        assert LinkedList.remove(linkedlist)