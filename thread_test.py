#test

import time
import threading

index = 0

def long_task() :
    global index
    index = index + 1
    for i in range(5) :
        time.sleep(1)
        print ( 'working : %s %d\n' % ( i , index) )
print('start')

threads = []

for i in range(5) :
    t  = threading.Thread( target = long_task )
    threads.append(t)

for t in threads :
    t.start()

for t in threads :
    t.join()

print('End')



