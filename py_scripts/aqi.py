#!/usr/bin/env python3
import sys
from datetime import timedelta

if len(sys.argv) < 3:
	print("Insufficient parameters !")
	print("Input format $./parser.py source destination")
	sys.exit(1)

src = open(sys.argv[1])
dst = open(sys.argv[2], 'w')

xtime = list()
count, no2, co2, co, dust, humid, temp, so2 = 0, 0, 0, 0, 0, 0, 0, 0

for line in src:
	buffer = line.rstrip("\n").split(",")
	xtime.append(buffer[1])
	no2 += float(buffer[2])
	co2 += float(buffer[3])
	co += float(buffer[4])
	dust += abs(float(buffer[5]))
	humid += float(buffer[6])
	temp += float(buffer[7])
	so2 += float(buffer[8])
	count += 1

	if count == 1200:

		dust /= 1200
		no2 /= 1200
		so2 /= 1200
		co /= 1200
		i_high, i_low, b_high, b_low = 0.0, 0.0, 0.0, 0.0

		if 0.0 <= dust <= 12:
			b_low, b_high, i_low, i_high = 0, 12, 0, 50
		elif 12.1 <= dust <= 35.4:
			b_low, b_high, i_low, i_high = 12.1, 35.4, 51, 100
		elif 35.5 <= dust <= 55.4:
			b_low, b_high, i_low, i_high = 35.5, 55.4, 101, 150
		elif 55.5 <= dust <= 150.4:
			b_low, b_high, i_low, i_high = 55.5, 150.4, 151, 200
		elif 150.5 <= dust <= 250.4:
			b_low, b_high, i_low, i_high = 150.5, 250.4, 201, 300
		elif 250.5 <= dust <= 350.4:
			b_low, b_high, i_low, i_high = 250.5, 350.4, 301, 400
		elif 350.5 <= dust <= 500.4:
			b_low, b_high, i_low, i_high = 350.5, 500.4, 401, 500
		else:
			pass

		si_dust = ((i_high - i_low) / (b_high - b_low)) * (dust - b_low) + i_low
		print("Dust ",si_dust)

		if 0.0 <= no2 <= 53:
			b_low, b_high, i_low, i_high = 0, 53, 0, 50
		elif 54 <= no2 <= 100:
			b_low, b_high, i_low, i_high = 54, 100, 51, 100
		elif 101 <= no2 <= 360:
			b_low, b_high, i_low, i_high = 101, 360, 101, 150
		elif 361 <= no2 <= 649:
			b_low, b_high, i_low, i_high = 361, 649, 151, 200
		elif 650 <= no2 <= 1249:
			b_low, b_high, i_low, i_high = 650, 1249, 201, 300
		elif 1250 <= no2 <= 1649:
			b_low, b_high, i_low, i_high = 1250, 1649, 301, 400
		elif 1650 <= no2 <= 2049:
			b_low, b_high, i_low, i_high = 1650, 2049, 401, 500
		else:
			pass

		si_no2 = ((i_high - i_low) / (b_high - b_low)) * (no2 - b_low) + i_low
		print("NO2 ",si_no2)

		if 0.0 <= so2 <= 35:
			b_low, b_high, i_low, i_high = 0, 35, 0, 50
		elif 36 <= so2 <= 75:
		 	b_low, b_high, i_low, i_high = 36, 75, 51, 100
		elif 76 <= so2 <= 185:
		 	b_low, b_high, i_low, i_high = 76, 185, 101, 150
		elif 186 <= so2 <= 304:
			b_low, b_high, i_low, i_high = 186, 304, 151, 200
		elif 305 <= so2 <= 604:
		 	b_low, b_high, i_low, i_high = 305, 604, 201, 300
		elif 605 <= so2 <= 804:
		 	b_low, b_high, i_low, i_high = 605, 804, 301, 400
		elif 805 <= so2 <= 1004:
		 	b_low, b_high, i_low, i_high = 805, 1004, 401, 500
		else:
		 	pass

		si_so2 = ((i_high - i_low) / (b_high - b_low)) * (so2 - b_low) + i_low
		print("SO2 ",si_so2)

		if 0.0 <= co <= 4.4:
			b_low, b_high, i_low, i_high = 0, 4.4, 0, 50
		elif 4.5 <= co <= 9.4:
			b_low, b_high, i_low, i_high = 4.5, 9.4, 51, 100
		elif 9.5 <= co <= 12.4:
			b_low, b_high, i_low, i_high = 9.5, 12.4, 101, 150
		elif 12.5 <= co <= 15.4:
			b_low, b_high, i_low, i_high = 12.5, 15.4, 151, 200
		elif 15.5 <= co <= 30.4:
			b_low, b_high, i_low, i_high = 15.5, 30.4, 201, 300
		elif 30.5 <= co <= 40.4:
			b_low, b_high, i_low, i_high = 30.5, 40.4, 301, 400
		elif 40.5 <= co <= 50.4:
			b_low, b_high, i_low, i_high = 40.5, 50.4, 401, 500
		else:
			pass

		si_co = ((i_high - i_low) / (b_high - b_low)) * (co - b_low) + i_low
		print("CO ",si_co)

		avg_time = str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), xtime)))//len(xtime)))
		high = str(max(si_co, si_no2, si_dust, si_so2))
		dst.write(avg_time + "," + high + "\n")

		count, no2, co2, co, dust, humid, temp, so2, zeros = 0, 0, 0, 0, 0, 0, 0, 0, 0
		xtime = []

	else:
		pass




dst.close()
src.close()