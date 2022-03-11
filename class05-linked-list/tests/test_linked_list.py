from class05_linked_list.linked_list import Node, LinkedList
import pytest

def test_empty():
    actual = LinkedList()
    expected = 'The linked-list is empty'
    assert str(actual) == str(expected)

def test_insert_one():
    emad = Node('Emad')
    ll = LinkedList()
    ll.insert(emad)
    actual = ll
    expected = '{ Emad } -> NULL'
    # print (type(actual))
    # print (type(expected))
    assert str(actual) == str(expected)

def test_insert_two():
    ll = LinkedList()
    ll.insert(Node('Emad'))
    ll.insert(Node('Anas'))
    actual = ll
    expected = '{ Anas } -> { Emad } -> NULL'
    assert str(actual) == str(expected)

def test_includes_head(my_ll):
    actual = my_ll.includes('Yazan')
    expected = True
    assert actual == expected

def test_includes_mid(my_ll):
    actual = my_ll.includes('Anas')
    expected = True
    assert actual == expected

def test_includes_last(my_ll):
    actual = my_ll.includes('Emad')
    expected = True
    assert actual == expected

def test_includes_false(my_ll):
    actual = my_ll.includes('test')
    expected = False
    assert actual == expected


@pytest.fixture
def my_ll():
    ll = LinkedList()
    ll.insert(Node('Emad'))
    ll.insert(Node('Anas'))
    ll.insert(Node('Yazan'))
    return ll