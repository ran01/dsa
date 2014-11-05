# -*- coding: utf-8 -*-
__author__ = 'qiangjun'
__last_update__ = "2014-10-22 21:35:28"

import random
import cProfile
import sys
sys.setrecursionlimit(100000)


def selection_sort_worst(seq):
    """
    non in-place
    """
    if len(seq) < 1:
        return seq
    result = []
    while seq:
        index = seq.index(min(seq))
        result.append(seq.pop(index))
    return result


def selection_sort_worse(lst):
    """
    still in-place
    """
    for i in range(0, len(lst)-1):
        rest = lst[i: len(lst)]
        idx_min = i+ rest.index(min(rest))
        lst[i], lst[idx_min] = lst[idx_min], lst[i]


def selection_sort(seq):
    """
    in-place sort
    """
    for i in range(0,len(seq)-1):
        idx_min = min(range(i,len(seq)), key=seq.__getitem__)
        seq[i], seq[idx_min] = seq[idx_min], seq[i]


def main():
    numbers =  [random.randrange(-100,100) for x in range(32)]
    print numbers
    selection_sort(numbers)
    print numbers


if __name__ == '__main__':
    cProfile.run('main()')