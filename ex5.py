# escape sequences
print "I am 5'8\" tall."

#\',\",\r,\n~~~new line,\t~~~sapce
print " "
print "list:\n\t*cat food\n\t*fish food\n\t*cup cake\n"
print "list:\ncat\n"
print "list:\rcat\n" # return to the first pointer and change from the second
print "list:\tcat\n"

import numpy as np
pi=np.pi
r=6378 #radium(km)
cir=2*pi*r*10**3 #circumference
print "The circumference of the Earth's equator in meters is:\n\t%sm."%cir

s=4*pi*r*r #surface area
print "The Earth's surface area is:\n\t%sm^2."%s
