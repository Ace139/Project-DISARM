#!/usr/bin/env python3
import sys

#if len(sys.argv) < 3:
#    print("Insufficient parameters !")
#    print("Input format $./parser.py source destination")
#    sys.exit(1)

src = open(sys.argv[1])
dst = open(sys.argv[2], 'w')

count, no2, co2, co, dust, humid, temp, lpg, smoke = 0, 0, 0, 0, 0, 0, 0, 0, 0

for line in src:
    buffer = line.rstrip("\n").split(",")
    no2 += float(buffer[2])
    co2 += float(buffer[3])
    co += float(buffer[4])
    dust += float(buffer[5])
    humid += float(buffer[6])
    temp += float(buffer[7])
    lpg += float(buffer[10])
    smoke += float(buffer[11])
    count += 1
    if count == 70:
        dst.write(buffer[0] + "," + buffer[1] + "," + str(no2/70) + "," + str(co2/70) + "," + str(co/70) + "," + str(dust/70) + "," + str(humid/70) + "," + str(temp/70) + "," + buffer[8] + "," + buffer[9] + "," + str(lpg/70) + "," + str(smoke/70) + "\n")
        count, no2, co2, co, dust, humid, temp, lpg, smoke = 0, 0, 0, 0, 0, 0, 0, 0, 0

dst.close()
src.close()