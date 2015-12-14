#!/usr/bin/env python

import sys
import math

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


def main():
    filename  = raw_input("[?] Enter encrypted text file name: ")
    output    = raw_input("[?] Enter decrypted output text file name: ")

    file      = open(str(filename), 'r')
    text      = file.read()
    decrypted = scytale_decrypt(text, 3)
    file.close()

    print "[i] Encrypted: \n %s \n" % (text)
    print "[i] Decrypted: \n %s \n" % (decrypted)

    file = open(str(output), 'w')
    file.write(decrypted)
    file.close()


if __name__ == '__main__':
    main()
