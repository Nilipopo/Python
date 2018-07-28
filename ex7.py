from sys import argv
script,first=argv
import numpy as np
pi=np.pi
r=float(first) #radium(km) & type conversion
cir=2*pi*r*10**3 #circumference
print "The circumference of the Earth's equator in meters is:\n\t%sm."%cir

#r=float(raw_input("Input the radium(km):\n\t"))
s=4*pi*r*r #surface area
print "The Earth's surface area is:\n\t%sm^2."%s
