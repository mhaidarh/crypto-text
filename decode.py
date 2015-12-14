#!/usr/bin/env python

from lib.decrypt import *

def main():
    filename  = raw_input("[?] Enter encrypted text file name: ")
    output    = raw_input("[?] Enter decrypted output text file name: ")
    key       = input("[?] Enter the key number (0-9): ")

    file      = open(str(filename), 'r')
    text      = file.read()
    file.close()
    decrypted = jefferson_decrypt(text)
    decrypted = scytale_decrypt(decrypted, key)

    print "[i] Encrypted: \n %s \n" % (text)
    print "[i] Decrypted: \n %s \n" % (decrypted)

    file = open(str(output), 'w')
    file.write(decrypted)
    file.close()


if __name__ == '__main__':
    main()
