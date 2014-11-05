# -*- coding: utf-8 -*-
__author__ = 'qiangjun'
__last_update__ = "2014-10-23 00:53:37"

import random
import cProfile
import sys

sys.setrecursionlimit(100000)


def heap_sort(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
    # in pseudo-code, heapify only called once, so inline it here
    for i in range(len(lst)/2-1, -1, -1):
        heapify(lst, i,len(lst)-1) 
    
    insert(lst, 5) 

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        heapify(lst, 0, end - 1)


def heapify(lst, i, end):
    while True:
        left = 2*i+1
        right = 2*i+2
        if left > end:
            break
        j = left
        if right <= end and lst[left] < lst[right]:
            j = right
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
            i = j
        else:
            break

def insert(lst, val):
    lst.append(val)
    i = len(lst)-1
    while i > 0:
        root = (i+1)/2-1
        if lst[i] > lst[root]:
            lst[i], lst[root] = lst[root], lst[i]
            i = root
        else:
            break


def main():
    numbers = [random.randrange(0,10) for x in range(10)]
    numbers = [6, 4, 4, 9, 9, 9, 2, 9, 0, 2]  # [0, 2, 2, 4, 4, 6, 9, 9, 9, 9]
    print numbers
    heap_sort(numbers)
    print numbers

if __name__ == '__main__':
    cProfile.run('main()')