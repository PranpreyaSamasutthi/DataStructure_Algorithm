#!/usr/bin/env python
# coding: utf-8

# In[13]:


import time
import math
import matplotlib.pyplot as plt
import random

############# Heap Sort #############

def Parent(i) :
    return math.floor(i/2)

def Left(i) :
    return 2*i

def Right(i) :
    return 2*i+1

def max_heapify(A,i) :
    l = Left(i)
    r = Right(i)
    #print(A)
    #print(f'left: {l}')
    #print(f'heap size: {heap_size}')
    #print(f'index: {i}')
    #print(f'right: {r}')
    
    if (l < heap_size and A[l] > A[i]) :
        largest = l
    else : largest = i
    
    if (r < heap_size and A[r] > A[largest]) :
        largest = r
    
    if largest != i :
        A[i],A[largest] = A[largest],A[i]  ##Exchange Values A[i] with A[largest]
        max_heapify(A, largest)

def build_max_heap(A) :
    heap_size = len(A)
    for i in range (math.floor(len(A)/2),0,-1) :
        max_heapify(A,i)
        
def heapsort(A) :
    build_max_heap(A)
    for i in range (len(A)-1,1,-1) :
        A[0],A[i] = A[i], A[0]
        heap_size = i
        max_heapify(A,0)
############# Heap Sort #############

############ Quick Sort ############
def partition(A,p,r) :
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quicksort (A,p,r):
    if p < r :
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
############ Quick Sort ############    
        
arr = [ 1, 11, 13, 5, 6, 7]
arr2 = [ 1, 11, 13, 5, 6, 7]
print(f'Array for Heap Sort: {arr}')
print(f'Array for Quick Sort: {arr2}')
heap_size = len(arr)
heapsort(arr)
quicksort(arr2,0,len(arr2)-1)
print('#'*30)
print(f'Heap Sorted: {arr}')
print(f'Quick Sorted: {arr2}')
    

    


# In[ ]:




