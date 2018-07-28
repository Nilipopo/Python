import numpy as np
pi=np.pi
def cal_r(cir):# Function: calculate radius
    return cir/(pi*2)

from sys import argv
script,first=argv
cir=float(first)
r=cal_r(cir)

if r>3396 and r<4887 or r<3396: #4887=(3396+6378)/2
    print "It's nearly Mars!"
elif r<6378 and r>4887 or r>6378:
    print "It's nearly Earth!"
else:
    print "It isn't near to both Mars and Earth!"
