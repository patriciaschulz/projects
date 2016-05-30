#!/usr/bin/env jython
# -*- coding: utf-8 -*-

import sys

v = open("notes.txt")
for line in v:
    sys.stdout.write(line)


v.close()
