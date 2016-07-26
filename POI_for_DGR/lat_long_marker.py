xdgr_lat = 23.5204
xdgr_long = 87.3119

dgr_lat = 23.4844
dgr_long = 87.3119

lat_shift = 0.00899
long_shift = 0.00979

'''
for i in range(4, 0, -1):
    #print(format(dgr_lat + i*lat_shift, '.4f'), end=',')
    print(dgr_lat, end=',')
    print(format(dgr_long + i*long_shift, '.4f'))

print('*' * 20)
'''
for i in range(1, 3):
    #print(format(dgr_lat - i*lat_shift, '.4f'), end=',')
    print(dgr_lat, end=',')
    print(format(dgr_long - i*long_shift, '.4f'))
