from math import floor
import sys
import time

print()
mytime = time.time()
hours = 0
minutes = 0
last_status = ''
def status_print(*args, size=0, current_file='done', **kwargs):
    last_status = ''
    hours = floor(round(time.time() - mytime)/3600)
    minutes = floor(round(time.time() - mytime)/60) - hours*60
    seconds = round(time.time() - mytime) - minutes*60 - hours*3600
    
    print(*args, **kwargs)
    print(' '*120)
    last_status = 'Elapsed time {0}:{1}:{2}, calculated memory {3}, loading {4}'.format(hours, minutes, seconds, size, current_file)
    print(last_status, end='\r')
    sys.stdout.write("\033[F")


