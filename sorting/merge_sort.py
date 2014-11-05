# -*- coding: utf-8 -*-
__author__ = 'qiangjun'
__last_update__ = '2014-10-23 00:33:00'

import random
import cProfile
import sys
sys.setrecursionlimit(100000)

def merge_sort(seq):
    """
    divide and divide , and merge 
    """
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left, right = seq[:mid], seq[mid:] 
    if len(left) > 1: 
        left = merge_sort(left)
    if len(right) > 1: 
        right = merge_sort(right)
    return merge(left,right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]: # change <= to >= will change the order of result
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:  # must do check, like: [] [x]
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def main():
    numbers =  [random.randrange(-100,100) for x in range(10020)]
    print numbers
    print merge_sort(numbers)

if __name__ == '__main__':
    cProfile.run('main()')