#!/usr/bin/python3
"""
 Minimum Operations 
"""


def minOperations(n):
    """ Returns the total """
    z, m = 0, 2
    while n > 1:
        while not n % m:
            z += m
            n /= m
        m += 1
    return z
