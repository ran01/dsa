# -*- coding: utf-8 -*-
__author__ = 'Qiangjun RAN'
__last_update__ = "2014-10-22 20:56:34"

import random
import cProfile
import sys
import math
sys.setrecursionlimit(10000)

def radix_sort(seq):
    """
    sorting intergers

    1. Devide input into two parts, one is non negative numbers >= 0,  and the other is negative numbers < 0.
    2. Each part sorts separately. and negative numbers to be treated as non negative numbers.
    3. After sorted, to reverse the negetive part, then append one to another.

    """
    negs = [i for i in seq if i < 0] # negative numbers
    non_negs = [i for i in seq if i >= 0] # non negative numbers
    if negs: 
        negs = sort_non_negs([abs(i) for i in negs])
        negs = [-i for i in negs[::-1]]
    if non_negs:
        non_negs = sort_non_negs(non_negs)
    return negs + non_negs


def sort_non_negs(seq):
    if len(seq) <=1 :
        return seq
    else:
        digits = len(str(max(seq)))
        seq = [(digits - len(str(i)))*'0'+str(i) for i in seq]  # padding with 0s, convert integers to strings
        for pos in range(digits-1, -1, -1):  # inverted order, low eight bit first.
            rlt = []
            for bit in range(10):  # radix is 10
                for num in seq: 
                    if int(num[pos]) == bit:
                        rlt.append(num)
            seq = rlt[:]
    return [int(i) for i in seq]



def radix_sort_improvement(seq):
    """
    support sorting float sequence
    """
    seq = [float(i) for i in seq]
    negs = [i for i in seq if i < 0]
    non_negs = [i for i in seq if i >= 0]
    if negs: 
        negs = sort_non_negs_float([abs(i) for i in negs])
        negs = [-i for i in negs[::-1]]
    if non_negs:
        non_negs = sort_non_negs_float(non_negs)
    return negs + non_negs



def sort_non_negs_float(seq):
    if len(seq) <=1 :
        return seq
    else:
        seq = [str(i).split('.') for i in seq]
        digits_left = len(max([i[0] for i in seq]))
        digits_right = len(max([i[1] for i in seq]))
        # padding with 0s both two sides, convert floats to strings
        seq = [(digits_left - len(str(i[0])))*'0'+str(i[0]) +'.'+ str(i[1])+ (digits_right - len(str(i[1])))*'0'  for i in seq]  
        # radix point skipped
        for pos in range(digits_left + digits_right, digits_left, -1) + range(digits_left-1, -1, -1):  
            rlt = []
            for bit in range(10): 
                for num in seq:
                    if int(num[pos]) == bit:
                        rlt.append(num)
            seq = rlt[:]
    return [float(i) for i in seq]


def main():
    numbers = [random.randrange(-10, 10) for x in range(20)]
    print numbers
    print radix_sort(numbers)
    numbers = [-8, -7, -1.33, -1.4, -7, -4, -1, 9.1, 5, -1.5, 7, 7, -6, 5, 5, -7, -5, 2, -6, 8]
    print numbers
    print radix_sort_improvement(numbers)

if __name__ == '__main__':
    cProfile.run('main()')