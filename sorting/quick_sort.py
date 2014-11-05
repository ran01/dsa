# -*- coding: utf-8 -*-

__author__ = "Qiangjun RAN"
__last_update__ = "2014-10-23 00:41:14"
import random
import cProfile
import sys

sys.setrecursionlimit(100000)

def quick_sort(seq):
    """
    to be done, in-place version
    """
    if len(seq) <= 1:
        return seq
    pivot = seq.pop()
    left = quick_sort([i for i in seq if i <= pivot])
    right = quick_sort([i for i in seq if i > pivot])
    left.append(pivot)
    left.extend(right)
    return left


def main():
    seq = [random.randrange(1, 11) for x in range(1024)]
    print seq
    print quick_sort(seq)

if __name__ == '__main__':
    cProfile.run('main()')