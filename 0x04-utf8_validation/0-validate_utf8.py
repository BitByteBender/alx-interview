#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid utf-8 encoding"""
    nbytes = 0

    for b in data:
        b = b & 0xFF

        if nbytes == 0:
            if b >> 5 == 0b110:
                nbytes = 1
            elif b >> 4 == 0b1110:
                nbytes = 2
            elif b >> 3 == 0b11110:
                nbytes = 3
            elif b >> 7:
                return False
        else:
            if b >> 0 != 0b10:
                return False
            nbytes -= 1
    return nbytes == 0
