#!/usr/bin/env python
# coding: utf-8

# In[118]:


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                #print(f'add {val} left parent{node.v}')
                node.l = Node(val)
                node.l.p = node
                #print(f' {val} under parent{node.l.p.v}')
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                #print(f'add {val} right parent{node.v}')
                node.r = Node(val)
                node.r.p = node
                #print(f' {val} under parent{node.r.p.v}')

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
            
    """def traverse_in_sorting_order(self):
        if self is not None:
            self._traverse_in_sorting_order(self.root)  #this will recursively exhaust all the left sides
                
    def _traverse_in_sorting_order(self, node):
        if node is None:
            return
        self._traverse_in_sorting_order(node.l)  #this will recursively exhaust all the left sides
        Sorted_Array.append(node.v)
        self._traverse_in_sorting_order(node.r)  #once the left side are exhausted, you can traverse the right node, and keep looking left.
    """
  
    def tree_Minimum(self,val):
        node = self.find(val)
        if self.root is not None and node is not None:
            return self._tree_Minimum(node)
        else:
            return None
        
    def _tree_Minimum(self, node):
        while (node.l is not None):
            node = node.l
        return node
    
    def tree_successor(self, val):
        node = self.find(val)
        if self.root is not None and node is not None:
            return self._tree_successor(node)
            
    def _tree_successor(self,node):
        if (node.r is not None):
            return self.tree_Minimum(node.r.v)
        y = node.p
        #print(f'Parent is {y.v}')  ----To check parent of current node
        #print(f'{node} and {y.r}') ----To check current node and the right parent node
        while y is not None and node == y.r:
            node = y
            y = y.p
            #print(f'y is {y.v}') ----To check y value
        return y
    
    
    
Sorted_Array = []
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.add(7)
tree.add(9)
tree.add(1)
tree.add(15)
tree.printTree()
print("*"*50)

#print(tree.find(3).v)
#print(tree.find(10))
#tree.deleteTree()
#tree.printTree()
#tree.traverse_in_sorting_order()
#print(f'Sorted BST: {Sorted_Array}')
value = input('Enter value in the BST to get Tree successor: ')
sucessor = tree.tree_successor(int(value))
print(f' Tree Successor of {value} is: ',end = "")
if sucessor is None:
    print('None')
else: print(sucessor.v)

