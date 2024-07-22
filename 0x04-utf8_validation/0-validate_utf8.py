#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding
"""


def get_leading_set_bits(num):
    """Determines if a given data set represents a valid UTF-8 encoding
    """
    bits = 0
    helply = 1 << 7
    while helply & num:
        bits += 1
        helply = helply >> 1
    return bits


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    bit = 0
    for i in range(len(data)):
        if bit == 0:
            bit = get_leading_set_bits(data[i])
            '''1-byte'''
            if bit == 0:
                continue
            '''Character can be 1 to 4 bytes long'''
            if bit == 1 or bit > 4:
                return False
        else:
            '''Current byte has format 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bit -= 1
    return bit == 0
