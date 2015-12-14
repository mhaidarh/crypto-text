#!/usr/bin/env python

import string
import math
import os

from random import Random

def scytale_encrypt(text, key):
    chars = [c for c in text if c not in (',','.','?','!',':',';',"'","(",")")]
    chunks = math.ceil(len(chars) / float(key))
    inters, i, j = [], 1, 1

    while i <= chunks:
        inters.append(tuple(chars[j - 1:(j + key) - 1]))
        i += 1
        j += key

    cipher, k = [], 0
    while k < key:
        l = 0
        while l < chunks:
            if k >= len(inters[l]):
                cipher.append('+')
            else:
                cipher.append(inters[l][k])
            l += 1
        k += 1

    return ''.join(cipher)


def jefferson_encrypt(string):
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


def main():
    filename  = raw_input("[?] Enter text file name: ")
    output    = raw_input("[?] Enter output text file name: ")
    key       = input("[?] Enter the key number (0-9): ")

    file      = open(str(filename), 'r')
    text      = file.read()
    file.close()
    encrypted = scytale_encrypt(text, key)
    encrypted = jefferson_encrypt(encrypted)

    print "[i] Text: \n %s \n" % (text)
    print "[i] Encrypted: \n %s \n" % (encrypted)

    file = open(str(output), 'w')
    file.write(encrypted)
    file.close()


if __name__ == '__main__':
    main()
