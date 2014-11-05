# -*- coding: utf-8 -*-
__author__ = 'Qiangjun RAN'
__last_update__ = "2014-10-23 00:44:07"

import random
import cProfile
import sys

sys.setrecursionlimit(100000)

def shell_sort(seq):
    """
    beautiful loop
    """
    gap = len(seq) // 2
    while gap:
        for idx, val in enumerate(seq):
            while idx >= gap and seq[idx - gap] > val:
                seq[idx] = seq[idx - gap]
                idx = idx - gap
            seq[idx] = val
        gap = 1 if gap == 2 else int(gap * 5.0 / 11)
    return seq

def main():
    numbers =  [random.randrange(-100,100) for x in range(20)]
    print numbers
    print shell_sort(numbers)

if __name__ == '__main__':
    cProfile.run('main()')