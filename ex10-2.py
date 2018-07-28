# function & calculate(difference of float & Earth's circumference & Mars circumference)
def float_diff(x1,x2):#compute the difference between two floats
    return x1-x2 # 4 retract
x=float(raw_input("Input float 1: "))
y=float(raw_input("Input float 2: "))
print "%s - %s = %s\n"%(x,y,float_diff(x,y))

import numpy as np
pi=np.pi
def cal_cir(r):#calculate circumference
    return 2*pi*r*10**3

r=float(raw_input("Input the radium(km) of Earth: ")) #radium(km) of Earth
print "The circumference of the Earth's equator is: %sm.\n"%cal_cir(r)

mr=3396 #radium(km) of Mars
print "The circumference of the Martian equator is: %sm."%cal_cir(mr)
