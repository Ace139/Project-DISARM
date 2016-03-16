from datetime import timedelta

times = ['00:58:00','00:59:00','01:00:00','01:01:00','01:02:00']

print(str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))//len(times))))