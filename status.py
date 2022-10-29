from math import floor
import sys
import time

print()
mytime = time.time()
hours = 0
minutes = 0
hours = floor(round(time.time() - mytime)/3600)
minutes = floor(round(time.time() - mytime)/60) - hours*60
seconds = round(time.time() - mytime) - minutes*60
def empty_print():
    print()
    sys.stdout.write("\033[F")
def status_print(*args, size=0, **kwargs):
    hours = floor(round(time.time() - mytime)/3600)
    minutes = floor(round(time.time() - mytime)/60) - hours*60
    seconds = round(time.time() - mytime) - minutes*60
    
    # sys.stdout.write("\033[F")
    print(*args, **kwargs)
    print(' '*80)
    print('Elapsed time {0}:{1}:{2}, calculated memory {3}'.format(hours, minutes, seconds, size), end='\r')
    
    sys.stdout.write("\033[F")
