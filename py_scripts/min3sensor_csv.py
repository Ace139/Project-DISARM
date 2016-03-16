#!/usr/bin/env python3

import sys

src = open(sys.argv[1])
des = open(sys.argv[2], 'w')

for line in src:
    buffer = line.rstrip("\n").split(",")
    lft = int(buffer[2])
    rgt = int(buffer[3])
    mid = int(buffer[4])
    des.write(buffer[0] + "," + buffer[1] + "," + str(min(lft, rgt, mid)) + "\n")

src.close()
des.close()