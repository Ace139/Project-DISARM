def convert(xtime):
	x = time.strptime(xtime,'%H:%M:%S')
	y = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
	return y

for i in range(1, 559):
	sec = convert(data.loc[i, 'Time']) - convert(data.loc[i-1, 'Time'])
	data.loc[i, 'Trend'] = data.loc[i - 1, 'Trend'] + sec

for i in range(559):
	if 120 <= data.loc[i, 'Value'] <= 160:
		data.loc[i, 'Bit'] = 1
	elif 60 <= data.loc[i, 'Value'] <= 90:
		data.loc[i, 'Bit'] = 2
	else:
		data.loc[i, 'Bit'] = 3