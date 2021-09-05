from collections import deque

def solution(n, t, m, timetable):
    timetable = sorted([int(time.split(':')[0])*60 + int(time.split(':')[1]) for time in timetable])
    last_time = 540 + (n-1)*t
    for i in range(n):
        if len(timetable) < m:
            return f'{last_time//60:02}:{last_time%60:02}'
        if i == n-1:
            if timetable[0] > last_time:
                return f'{last_time//60:02}:{last_time%60:02}'
            else:
                return f'{(timetable[m-1]-1)//60:02}:{(timetable[m-1]-1)%60:02}'
        for j in range(m-1,-1,-1):
            bus_time = 540 + i*t
            if timetable[j] <= bus_time:
                del timetable[j]