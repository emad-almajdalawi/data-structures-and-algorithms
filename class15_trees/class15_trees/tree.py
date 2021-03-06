class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, new_value):
        '''
        A method to add a node to the stack
        Input: new_value
        '''
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node
    

    def pop(self):
        '''
        A method to remove a node from the stack
        Input: nothing
        '''
        if self.is_empty():
            return 'The stack is empty'
        current = self.top
        self.top = self.top.next
        current.next = None
        return current.value
    

    def is_empty(self):
        '''
        A method to check if the stack is empty or not
        Input: nothing
        Output: boolian (True if the stack is empty)
        '''
        if self.top is None:
            return True
        else:
            return False
    
    def peek(self):
        '''
        A method to show the top of the stack
        '''
        if self.is_empty():
            return 'The stack is empty'
        else:
            return self.top.value
      

class Queue:
    '''
    A class to creat a queue
    Input: no input
    constructor: front node, rear node
    '''

    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, new_value):
        '''
        A method to add a node to the queue (to the rear)
        Input: new value
        '''
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        '''
        A method to remove a node from the queue (from front)
        Input: nothing
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            self.front = self.front.next
            current.next = None
        return current.value


    
    def peek(self):
        '''
        A method to show the front of the queue
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.front.value
    

    def is_empty(self):
        '''
        A method to check if the queue is empty or not
        Input: nothing
        Output: boolian (True if the queue is empty)
        '''
        if self.front is None:
            return True
        else:
            return False

    def __str__(self):
        '''
        A method to print the queue
        Input: nothing
        Output: string
        '''
        output = ''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output


class TNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right=None


class BinaryTree:

    def __init__(self):
        self.root = None
        self.maximum = 0
        self.sum = 0
        self.count = 0
        self.arr = []
    

    def pre_order_recursive(self):
        """
        A method to traverse a tree in pre-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            values.append(current.value)
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)

        _walk(current)
        return values


    def in_order_recursive(self):
        """
        A method to traverse a tree in in-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            if current.left:
                _walk(current.left)
            values.append(current.value)
            if current.right:
                _walk(current.right)

        _walk(current)
        return values


    def post_order_recursive(self):
        """
        A method to traverse a tree in post-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)
            values.append(current.value)

        _walk(current)
        return values


    def pre_order(self):
        """
        A method to traverse the tree elements in pre-order
        input: None
        output: print a list of the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()
        stack.push(current)
        while not stack.is_empty():
            current = stack.pop()
            values.append(current.value)
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
        return values
    

    def in_order(self):
        """
        A method to traverse the tree elements in in-order
        input: None
        output: print a list of  the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()
        while True:
            if current is not None:
                stack.push(current)
                current = current.left
            elif not stack.is_empty():
                current = stack.pop()
                values.append(current.value)
                current = current.right
            else:
                break
        return values

    
    def post_order(self):
        """
        A method to traverse the tree elements in post-order
        input: None
        output: print a list of  the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()  
        while True:
            while current is not None:
                if current.right is not None:
                    stack.push(current.right)
                stack.push(current)
                current = current.left
            current = stack.pop()
            if current.right is not None and stack.peek() == current.right:
                stack.pop()
                stack.push(current)
                current = current.right
            else:
                values.append(current.value)
                current = None
            if stack.is_empty():
                break
        return values

    
    def maximum_value(self):
        """
        A method to find the max value of a binary tree
        input: None
        output: max value
        """
        # The max method for binary search tree is in BinarySearchTree class

        # space O(1)
        current = self.root
        if current is None: return 'The tree is empty'
        self.maximum = current.value

        def _walk(current):
            self.maximum = current.value if current.value > self.maximum else self.maximum
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)

        _walk(current)
        return self.maximum
        
        ## or space O(n)
        # all_elements = self.pre_order()
        # if type(all_elements) != list or all_elements == []: return 'The tree is empty' 
        # return max(all_elements)


    def sum_odd_numbers_binary(self):
        '''
        A method to find the summation of odd values in a binary tree
        input: None
        output: sum of odd values
        '''
        current = self.root
        if current is None: return 'The tree is empty'
        self.sum = 0

        def _walk(current):
            if current.value % 2 != 0:
                self.sum += current.value
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)

        _walk(current)
        return self.sum


    def tree_symitrice(self, tree):
        '''
        Check if the tree is symitric
        input: tree
        output: True or False
        '''
        if tree.root is None:
            raise Exception ('Empty tree!')

        arr = self.arr = [ ]
        current = tree.root
        
        def _walk(current):       # in order, left > root > right
            if current.left:
                _walk(current.left)
            arr.append(current.value) 
            if current.right:
                _walk(current.rught)
        _walk(current)
        
        counter = 0
        for i in len(arr):
            if arr[i] != arr[i-counter]:
                    return False
            count += 1
        return True




def file_folder_check( binary_tree1, binary_tree2):
    '''
    A method to check if the number of files and the number of folders are simmiler in two binary trees
    input: two binary trees
    output: True or False
    '''
    if binary_tree1.root is None or binary_tree2.root is None: return False
    files = []
    folders =[]
    
    def _walk(current):
        if current.left:
            _walk(current.left)
        if current.right:
            _walk(current.right)
        if not current.right and not current.left:              
            files.append(current.value)
        else:
            folders.append(current.value)
            
    _walk(binary_tree1.root)
    tree1_file_count = len(files)
    tree1_folder_count = len(folders)

    files = []
    folders =[]
    _walk(binary_tree2.root)
    tree2_file_count = len(files)
    tree2_folder_count = len(folders)

    if tree1_file_count == tree2_file_count and tree1_folder_count == tree2_folder_count:
        return True
    return False




        

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    

    def insert(self, new_value):
        """
        A method to insert a node to the tree
        input: value
        output: None
        """
        if type(new_value) is TNode or type(new_value) is Node:
            return 'Please enter a value, it will be converted automaticly to TNode'
        if self.root is None:
            self.root = TNode(new_value)
        else:
            current = self.root
            while True:
                if new_value == current.value: return 'value is already exist'
                elif new_value < current.value:
                    if current.left is None:
                        current.left = TNode(new_value)
                        break
                    else:
                        current = current.left
                elif new_value > current.value:
                    if current.right is None:
                        current.right = TNode(new_value)
                        break
                    else:
                        current = current.right
                else:
                    break
    

    def find(self, value):
        """
        A method to find a node in the tree
        input: value
        output: True if the node is in the tree, False if not
        """
        current = self.root
        if current is None: return 'The tree is empty'
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False


    def max_binary_search(self):
        """
        A method to find the max value of a binary search tree
        input: None
        output: max value
        """
        current = self.root
        if current is None: return 'The tree is empty'
        if current.right is None: return current.value
        while current.right is not None:
            current = current.right
            if current.right is None:
                return current.value


# Not a task nor a strech goal
    def delete_binary_search(self, value):
        """
        A method to delete a leaf node from the the tree, or to delete a parent of a leaf only if that parent has only one child
        input: value
        output: The deleted value
        """
        if self.root is None:
            return 'The tree is empty'
        else:
            current = self.root
            parent = None
            while current:
                if value < current.value:
                    parent = current
                    current = current.left
                elif value > current.value:
                    parent = current
                    current = current.right
                else:
                    if current.left is None and current.right is None:
                        if parent.left == current:
                            parent.left = None
                            return current.value
                        elif parent.right == current:
                            parent.right = None
                            return current.value
                    # The below is to delete a parent of a leaf only if that parent has only one child
                    elif current.left is None:
                        if parent.left == current:
                            parent.left = current.right
                            return current.value
                        elif parent.right == current:
                            parent.right = current.right
                            return current.value
                    elif current.right is None:
                        if parent.left == current:
                            parent.left = current.left
                            break
                        elif parent.right == current:
                            parent.right = current.left
                            return current.value


    def get_successor(self, value):
        """
        A method to find the successor of a node in the tree (smallest value that is greater than the value)
        input: value
        output: successor value
        """
        if self.root is None:
            raise ValueError("The tree is empty")
        current = self.root
        parent = None
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.right:
                    current = current.right
                    while current.left :
                        current = current.left
                    return current.value
                else:
                    return parent.value


    def get_predecessor(self, value):
        """
        A method to find the predecessor of a node in the tree (largest value that is less than the value)
        input: value
        output: predecessor value
        """
        if self.root is None:
            raise ValueError("The tree is empty")
        current = self.root
        parent = None
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left is not None:
                    current = current.left
                    while current.right:
                        current = current.right
                    return current.value
                else:
                    return parent.value


def breadth_first_binary(tree):
    '''
    A method to traverse the binary-tree elements (breadthFirst)
    input: tree
    output: print a list of the value of each node
    '''
    if not isinstance(tree, BinarySearchTree):
        if not isinstance(tree, BinaryTree):
            raise Exception ('Please enter a BinarySearchTree or BinaryTree')
    current = tree.root
    if current is None: raise Exception('The tree is empty')
    values = []
    queue = Queue()
    queue.enqueue(current)
    while not queue.is_empty():
        current = queue.dequeue()
        values.append(current.value)
        if current.left is not None:
            queue.enqueue(current.left)
        if current.right is not None:
            queue.enqueue(current.right)
    return values






     

        



if __name__ == '__main__':

    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node3
    node1.right = node2
    node3.left = node4
    tree = BinaryTree()
    tree.root = node1
    # tree.pre_order()
    # print(tree.maximum_value())
    print(breadth_first_binary(tree))

    tree2 = BinarySearchTree()
    tree2.insert(5)
    tree2.insert(2)
    tree2.insert(1)
    tree2.insert(3)
    tree2.insert(10)
    tree2.insert(7)
    tree2.insert(12)
    tree2.delete_binary_search(1)
    tree2.delete_binary_search(2)

    # print('aaaaaaaa', isinstance(tree2, BinarySearchTree))

    print(tree2.pre_order())
    print(tree2.pre_order_recursive())
    print(tree2.find(10))
    print(tree2.in_order())
    print(tree2.in_order_recursive())
    print(tree2.find(15))
    print(tree2.post_order())
    print(tree2.post_order_recursive())
    print(breadth_first_binary(tree2))

    print(tree2.maximum_value())
    print(tree2.max_binary_search())
   

    tree3 = BinarySearchTree()
    [tree3.insert(i) for i in [5,2,1,3,10,7,12, 15, 4]]
    print(tree3.pre_order())

    print(tree.sum_odd_numbers_binary())
    print(file_folder_check(tree,tree2))
    print(file_folder_check(tree2,tree2))


    BST = BinarySearchTree()
    BST.insert(41)
    BST.insert(5)
    BST.insert(6)
    BST.insert(20)
    BST.insert(22)
    BST.insert(25)
    BST.insert(47)
    BST.insert(58)
    BST.insert(60)
    BST.insert(69)
    BST.insert(74)
    BST.insert(96)
    BST.insert(92)
    BST.insert(84)

    print(BST.get_successor(25))
    print(BST.get_successor(41))

    print(BST.get_predecessor(74))
    print(BST.get_predecessor(47))
