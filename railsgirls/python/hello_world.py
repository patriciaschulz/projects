#!/usr/bin/env jython
# -*- coding: utf-8 -*-

for i in range (2,101):
    is_prime = True
    for j in range (2,i):
        if i%j == 0:
            # j is divisor of i, so i is not prime
            is_prime = False

    if is_prime:
        print i
