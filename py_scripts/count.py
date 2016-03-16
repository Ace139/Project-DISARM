#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Insufficient Parameters!")
    print("Input formar $./count.py filename.csv")
    sys.exit(1)

src = open(sys.argv[1])

n1, n2, n3, cnt = 0, 0, 0, 0

for line in src:
    cnt += 1
    buffer = line.rstrip("\n").split(",")
    if 60 <= int(buffer[1]) <= 90:
        n1 += 1
    else:
        pass
    if 60 <= int(buffer[2]) <= 90:
        n2 += 1
    else:
        pass
    if 60 <= int(buffer[3]) <= 90:
        n3 += 1
    else:
        pass

print("Number of data : ",cnt)
print("Pings from S1: %d, S2:%d, S3:%d" %(n1, n2, n3))
