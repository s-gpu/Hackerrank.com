#!/usr/bin/python3

time = input()
if time[-2:] == 'PM' and time[:2] == '12':
    time = '12' + time[2:-2]
elif time[-2:] == 'AM' and time[:2] == '12':
    time = '00' + time[2:-2]
elif time[-2:] == 'PM':
    time = str(int(time[:2]) + 12) + time[2:-2]
else:
    time = time[:-2]
print(time)
