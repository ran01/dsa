# -*- coding: utf-8 -*-
__author__ = 'qiangjun'

import random
import cProfile
import sys

sys.setrecursionlimit(100000)

def insertion_sort(seq):
    for idx, val in enumerate(seq):
        while idx >= 1 and seq[idx-1] > val:
            seq[idx] = seq[idx-1]
            idx = idx - 1
        seq[idx] = val
    return seq


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted        
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]
 
 
import bisect
def insertion_sort_bin_use_lib(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)

def main():
    numbers = [random.randrange(0,10) for x in range(10)]
    # numbers = [2,4,6,7,5,3]
    print numbers
    n = insertion_sort(numbers)
    print n

if __name__ == '__main__':
    cProfile.run('main()')