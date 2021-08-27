#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import math
import matplotlib.pyplot as plt
import random

def find_max_crossing_subarray (A, low, mid, high):
    #Left side
    left_sum = float('-inf')
    sum = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    #Right side
    right_sum = float('-inf')
    sum = 0
    max_right = 0
    for j in range(mid+1,high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    #return L R C
    return max_left, max_right, left_sum+right_sum

def find_maximum_subarray (A, low, high):
    if high == low: return (low,high,A[low])
    else: 
        mid = math.floor((low+high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)               #for left
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)         #for right
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high) #for cross
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
        
def get_spent_time(A):
    #start time
    time_start = time.time()
    result = find_maximum_subarray(A,0,len(A)-1)
    n = len(A)
    n_list.append(n) 
    #get time after finding maximum subarray
    spent_time = time.time() - time_start
    total_time.append(spent_time)
    #get converted time from theoretical complexity 
    c = 1/500000
    nlgn_total_time.append(c*n*math.log2(n))
    #get result list
    result_list.append(result)
    
#declare variables
n_list = []
total_time = []
nlgn_total_time = []
result_list = []

    
Array100 = [random.randint(-10,10) for i in range(10000)]        
Array1000 = [random.randint(-10,10) for i in range(10000)]
Array10000 = [random.randint(-10,10) for i in range(10000)]
Array100000 = [random.randint(-10,10) for i in range(100000)]
Array1000000 = [random.randint(-10,10) for i in range(1000000)]
Array10000000 = [random.randint(-10,10) for i in range(1000000)]

get_spent_time(Array100)
get_spent_time(Array1000)
get_spent_time(Array10000)
get_spent_time(Array100000)
get_spent_time(Array1000000)
#get_spent_time(Array10000000)

print(total_time)

#Plot the graph
fig = plt.figure()
p = fig.add_subplot(1,1,1)
#p.set_yscale('log')
#p.set_xscale('log')

p.plot(n_list, total_time, label = 'Time Spent')
p.plot(n_list, nlgn_total_time, label = 'theoretical complexity')
p.legend(loc='best')

