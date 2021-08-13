#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as rd
import math

def insertionSort(Arr):
    # Check Length of Input
    if int(len(Arr)) > 1 :
        i = 1

        #Loop for each index of Array
        while i < len(Arr):
            Arr_Val = Arr[i]    
            j = i-1

            #check all the previous values compared to A[i]
            while j >= 0 and Arr_Val < Arr[j] :
                Arr[j+1] = Arr[j]
                j = j-1
            
            Arr[j+1] = Arr_Val
            i = i+1          

def mergeSort(Arr):
    if len(Arr) > 1:
 
        #Get the middle for spliting
        mid = math.ceil(len(Arr)/2)

        #Split into 2 Arrays
        L = Arr[:mid]
        R = Arr[mid:]

        #Recursive Merging
        mergeSort(L)
        mergeSort(R)

        #Initial index of L,R, and Arr
        i = 0
        j = 0
        k = 0

        #Compare within Array
        while (i < len(L) and j < len(R)):
            ### Check Comparing
            #print(f'{L[i]} with {R[j]}')
            if L[i] < R[j]:
                Arr[k] = L[i]
                i=i+1
            else:
                Arr[k] = R[j]
                j=j+1

            k=k+1

        #Insert remaining elements
        while i < len(L):
            Arr[k] = L[i]
            i=i+1
            k=k+1

        while j < len(R):
            Arr[k] = R[j]
            j=j+1
            k=k+1

        ### Check elements of Arrays
        #print(L)
        #print(R)
        #print(Arr)
        #print('*'*20)
 


Test_Arr = rd.sample(range(1,100),5)
print(f'Input Array: {Test_Arr}')
insertionSort(Test_Arr)
print(f'Insertion Sorted Array: {Test_Arr}')
print('='*30)

Test_Arr2 = rd.sample(range(1,100),5)
print(f'Input Array: {Test_Arr2}')
mergeSort(Test_Arr2)
print(f'Merge Sorted Array: {Test_Arr2}')

