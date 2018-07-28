print "Which planet do you want to choose? Input 1~~~Earth 2~~~Mars"
ch=raw_input()

if ch==1:
    r=6378
else:
    r=3396

print "Check the radius~~~Input '*.radius()'\nthe result~~~Input '*.result()'"

def radius():
    print r,"km."

import numpy as np
pi=np.pi
def cal_cir(r):#calculate circumference
    return 2*pi*r*10**3
def result():
    print "The circumference of equator is: %sm."%cal_cir(r)
