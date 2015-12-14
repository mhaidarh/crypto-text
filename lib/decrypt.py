#!/usr/bin/env python

import string
import math
import os

from random import Random

def scytale_decrypt(cipher_text, key):
    chars = [c for c in cipher_text]
    chunks = int(math.ceil(len(chars) / float(key)))
    inters, i, j = [], 1, 1

    while i <= key:
        inters.append(tuple(chars[j - 1:(j + chunks) -1]))
        i += 1
        j += chunks

    plain, k = [], 0
    while k < chunks:
        l = 0
        while l < len(inters):
            plain.append(inters[l][k])
            l += 1
        k += 1

    return ''.join(plain)


def jefferson_decrypt(string):
    result = ""
    # Loop over characters
    for v in string:
        # Convert to number with ord
        c = ord(v)
        # Shift number back or forward
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        # Append to result.
        result += chr(c)
    # Return transformation.
    return result
