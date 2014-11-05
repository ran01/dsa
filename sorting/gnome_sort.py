# -*- coding: utf-8 -*-

__author__ = 'qiangjun'
__last_update__ = '2014-10-23 00:27:37'

import random
import cProfile

def gnomesort(seq):
    """
    gnome sort depends on the reversed pair's count.
    suit for nearly sorted 
    """
    if len(seq) <= 1:
        return seq
    i = 0  # start from index 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i = i + 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i = i - 1

def main():
    numbers =  [random.randrange(1,11) for x in range(3)]
    gnomesort(numbers)
    print numbers

if __name__ == '__main__':
    cProfile.run('main()')