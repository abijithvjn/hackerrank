#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the countSubstrings function below.
#
def countSubstrings(s, queries):
    result1 =[]
    for i in queries:
        result=[]
        substring = s[i[0]:(i[1]+1)]
        elementset =[]
        len1 = len(substring)
        result = ("".join(substring[j:k+1]) for j in  range(len1) for k in range (j,len1))
        result1.append(len(set(result)))
    return(result1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = raw_input().split()

    n = int(nq[0])

    q = int(nq[1])

    s = raw_input()

    queries = []

    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    result = countSubstrings(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
