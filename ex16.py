# Control structure

# if
cats,dogs=raw_input("Input the number of cats and dogs: ").split()
if cats<dogs:
    print "More dogs than cats.\n"
elif dogs<cats:
    print "More cats than dogs.\n"
else: # always pair an if with an else
    print "Same number of cats and dogs.\n"

# for
a=[1,2,3]
for i in a:
    print i
    print 1+3
for i in range(3):
    print a[i] # a cannot be a set!

aa={1,2,3}
b={1:'a',2:'b',3:'c'}
for i in aa:
    print b[i]
print '\n'

# while ~~~~~ not know times
i=0
while i<21: # condition
    print "I love you!", # , can horizontally display
    i=i+1
print '\n'
 
# while & random 
import numpy as np
i=1
k=0
print i
while i>0:
    i=np.random.randn(1) # Gaussian distribution
    print i
    k=k+1
print k
