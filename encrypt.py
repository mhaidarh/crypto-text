#!/usr/bin/env python

import sys
import math

def scytale_encrypt(plain_text, key):
    #chars = [c.upper() for c in plain_text if c not in (' ',',','.','?','!',':',';',"'","(",")")]
    chars = [c for c in plain_text]
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


def main():
    filename  = raw_input("[?] Enter text file name: ")
    output    = raw_input("[?] Enter output text file name: ")

    file      = open(str(filename), 'r')
    text      = file.read()
    encrypted = scytale_encrypt(text, 3)
    file.close()

    print "[i] Text: \n %s \n" % (text)
    print "[i] Encrypted: \n %s \n" % (encrypted)

    file = open(str(output), 'w')
    file.write(encrypted)
    file.close()


if __name__ == '__main__':
    main()
