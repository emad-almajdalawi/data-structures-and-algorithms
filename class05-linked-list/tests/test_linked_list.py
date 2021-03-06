from class05_linked_list.linked_list import Node, LinkedList, DNode, DoublyLinkedList, merge_liked_list
import pytest

def test_empty():
    actual = str(LinkedList())
    expected = 'The linked-list is empty'
    assert actual == expected

def test_insert_Node(my_ll):
    actual = my_ll.insert(Node('Emad'))
    expected = 'please enter a value, it will be converted to Node automaticly'
    assert actual == expected

def test_insert_one():
    ll = LinkedList()
    ll.insert('Emad')
    actual = str(ll)
    expected = '{ Emad } -> NULL'
    assert actual == expected

def test_insert_two():
    ll = LinkedList()
    ll.insert('Emad')
    ll.insert('Anas')
    actual = str(ll)
    expected = '{ Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_var():
    ll = LinkedList()
    emad = 'Emad'
    ll.insert(emad)
    actual = str(ll)
    expected = '{ Emad } -> NULL'
    assert actual == expected  

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



def test_append():
    ll = LinkedList()
    ll.append('Emad')
    ll.append('Anas')
    actual = str(ll)
    expected = '{ Emad } -> { Anas } -> NULL'
    assert actual == expected

def test_append_Node(my_ll):
    actual = my_ll.append(Node('Emad'))
    expected = 'please enter a value, it will be converted to Node automaticly'
    assert actual == expected

def test_insert_after_head(my_ll):
    my_ll.insert_after('Yazan', 'after head')
    actual = str(my_ll)
    expected = '{ Yazan } -> { after head } -> { Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_after_tail(my_ll):
    my_ll.insert_after('Anas', 'in the mid')
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> { in the mid } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_after_tail(my_ll):
    my_ll.insert_after('Emad', 'after tail')
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> { Emad } -> { after tail } -> NULL'
    assert actual == expected

def test_insert_after_something_outside_list(my_ll):
    actual = my_ll.insert_after('111', 'insertion')
    expected = 'This value does not exist in this linked list!'
    assert actual == expected

def test_insert_after_Node(my_ll):
    actual = my_ll.insert_after('Emad' ,Node('Emad'))
    expected = 'please enter a value, it will be converted to Node automaticly'
    assert actual == expected

def test_insert_before_head(my_ll):
    my_ll.insert_before('Yazan', 'after head')
    actual = str(my_ll)
    expected = '{ after head } -> { Yazan } -> { Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_before_tail(my_ll):
    my_ll.insert_before('Anas', 'in the mid')
    actual = str(my_ll)
    expected = '{ Yazan } -> { in the mid } -> { Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_before_tail(my_ll):
    my_ll.insert_before('Emad', 'before tail')
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> { before tail } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_before_True(my_ll):
    my_ll.insert_before('Emad', True)
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> { True } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_before_False(my_ll):
    my_ll.insert_before('Emad', False)
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> { False } -> { Emad } -> NULL'
    assert actual == expected

def test_insert_brfore_something_outside_list(my_ll):
    actual = my_ll.insert_before('111', 'insertion')
    expected = 'This value does not exist in this linked list!'
    assert actual == expected

def test_insert_before_Node(my_ll):
    actual = my_ll.insert_before('Emad' ,Node('Emad'))
    expected = 'please enter a value, it will be converted to Node automaticly'
    assert actual == expected

def test_kth_from_end_last_index(my_ll):
    actual = my_ll.kth_from_end(2)
    expected = 'Yazan'
    assert actual == expected

def test_kth_from_end_first_index(my_ll):
    actual = my_ll.kth_from_end(0)
    expected = 'Emad'
    assert actual == expected

def test_kth_from_end_outside_list(my_ll):
    actual = my_ll.kth_from_end(5)
    expected = 'Index not found!'
    assert actual == expected

def test_kth_from_end_empty():
    ll = LinkedList()
    actual = ll.kth_from_end(1)
    expected = 'The linked-list is empty'
    assert actual == expected




def test_merge_liked_list():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('B')
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('2')
    my_l_list_2.insert('1')
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = '{ A } -> { 1 } -> { B } -> { 2 } -> NULL'
    assert actual == expected

def test_merge_liked_list_first_longer():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('D')
    my_l_list_1.insert('C')
    my_l_list_1.insert('B')
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('2')
    my_l_list_2.insert('1')
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = '{ A } -> { 1 } -> { B } -> { 2 } -> { C } -> { D } -> NULL'
    assert actual == expected    

def test_merge_liked_list_second_longer():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('B')
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('4')
    my_l_list_2.insert('3')
    my_l_list_2.insert('2')
    my_l_list_2.insert('1')
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = '{ A } -> { 1 } -> { B } -> { 2 } -> { 3 } -> { 4 } -> NULL'
    assert actual == expected    

def test_merge_liked_list_both_empty():
    my_l_list_1 = LinkedList()
    my_l_list_2 = LinkedList()
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = 'The linked-lists are empty'
    assert actual == expected

def test_merge_liked_list_first_empty():
    my_l_list_1 = LinkedList()
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('2')
    my_l_list_2.insert('1')
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = '{ 1 } -> { 2 } -> NULL'
    assert actual == expected

def test_merge_liked_list_second_empty():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('B')
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    actual = str(merge_liked_list(my_l_list_1, my_l_list_2))
    expected = '{ A } -> { B } -> NULL'
    assert actual == expected

def test_merge_liked_list_type1():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('1')
    actual = str(merge_liked_list(my_l_list_1, 1))
    expected = 'Please make sure that the entered data type is LinkedList for both arguments'
    assert actual == expected

def test_merge_liked_list_type2():
    my_l_list_1 = LinkedList()
    my_l_list_1.insert('A')
    my_l_list_2 = LinkedList()
    my_l_list_2.insert('1')
    actual = str(merge_liked_list('A', my_l_list_2))
    expected = 'Please make sure that the entered data type is LinkedList for both arguments'
    assert actual == expected


# **************************
# *        streach         *
# **************************

def test_dll_empty():
    actual = str(DoublyLinkedList())
    expected = 'The linked-list is empty'
    assert actual == expected

def test_dll_insert_one():
    dll = DoublyLinkedList()
    dll.insert('Emad')
    actual = str(dll)
    expected = '{ Emad } -> NULL'
    assert actual == expected

def test_dll_insert_two():
    dll = DoublyLinkedList()
    dll.insert('Emad')
    dll.insert('Anas')
    actual = str(dll)
    expected = '{ Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_dll_insert_Dnode():
    dll = DoublyLinkedList()
    dll.insert(DNode('Emad'))
    actual = str(dll)
    expected = 'please enter a value, it will be converted to (DNode) node automaticly'




def test_delete_head(my_ll):
    my_ll.delete_node('Yazan')
    actual = str(my_ll)
    expected = '{ Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_delete_mid(my_ll):
    my_ll.delete_node('Anas')
    actual = str(my_ll)
    expected = '{ Yazan } -> { Emad } -> NULL'
    assert actual == expected

def test_delete_tail(my_ll):
    my_ll.delete_node('Emad')
    actual = str(my_ll)
    expected = '{ Yazan } -> { Anas } -> NULL'
    assert actual == expected

def test_delete_something_outside_list(my_ll):
    actual = my_ll.delete_node('111')
    expected = 'This value does not exist in this linked list!'
    assert actual == expected

def test_find_mid_odd(my_ll):
    actual = my_ll.find_mid()
    expected = 'Anas'
    assert actual == expected

def test_find_mid_even(my_ll):
    ll = LinkedList()
    ll.append('test')
    actual = my_ll.find_mid()
    expected = 'Anas'
    assert actual == expected




@pytest.fixture
def my_ll():
    ll = LinkedList()
    ll.insert('Emad')
    ll.insert('Anas')
    ll.insert('Yazan')
    return ll