#!/usr/bin/python3
""" Minimum Operations"""

def minOperations(n: int) -> int:
    """ Minimum Operations needed"""
    next = 'H'
    boody = 'H'
    k = 0
    while (len(boody) < n):
        if n % len(boody) == 0:
            k += 2
            next = boody
            boody += boody
        else:
            k += 1
            boody += next
    if len(boody) != n:
        return 0
    return k
