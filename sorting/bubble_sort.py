__author__ = 'qiangjun'
__last_update__ = "2014-10-22 21:11:59"

import random
import cProfile
import sys
sys.setrecursionlimit(100000)


def bubble_sort(seq):
    """
    in-place sort, from left to right
    """
    len_seq = len(seq)
    if len_seq <= 1:
        return seq
    for i in range(len_seq-1):
        for j in range(i, len_seq):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]


def bubble_sort_from_right_to_left(seq):
    len_seq = len(seq)
    if len_seq <= 1:
        return seq
    for i in range(len_seq-1,-1,-1): 
        for j in range(i):
            if seq[i] < seq[j]:
                seq[i], seq[j] = seq[j], seq[i]


def main():
    numbers =  [random.randrange(1,10) for x in range(10)]
    print numbers
    bubble_sort(numbers)
    print numbers
    numbers =  [random.randrange(10,100) for x in range(10)]
    print numbers
    bubble_sort_from_right_to_left(numbers)
    print numbers

if __name__ == '__main__':
    cProfile.run('main()')
    