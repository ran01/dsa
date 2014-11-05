# -*- coding: utf-8 -*-
__author__ = 'qiangjun'
__last_update__ = '2014-10-23 00:16:38'

import random
import cProfile
import sys
sys.setrecursionlimit(100000)

def bucket_sort(seq):
    """
    only supporting to sort integers, not in-place, neither stable
    space complexity depends on buckets count , or the span between the min value and the max value of seq

    """
    if len(seq) <= 1:
        return seq
    min_num, max_num = min(seq), max(seq)
    size = max_num - min_num + 1  # bucket size
    buckets = [0 for i in range(size)]  # init buckets
    for num in seq:
        buckets[num-min_num] = buckets[num-min_num] + 1 # one to one map and fill buckets
    result = []
    for idx, val in enumerate(buckets):
        if val:  # not init val 0
            result.extend([idx+min_num]*val)
    return result

def main():
    numbers =  [random.randrange(-10,10) for x in range(20)]
    print numbers
    print bucket_sort(numbers)

if __name__ == '__main__':
    cProfile.run('main()')