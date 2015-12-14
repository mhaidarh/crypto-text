#!/usr/bin/env python

from lib.encrypt import *

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
