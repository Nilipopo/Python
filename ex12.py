# list & tuple & range
aa=[1,2,3,'a','b','c'] #list
bb=(1,2,3,'a','b','c') #tuple
cc=range(0,10,2) #range(first,last(not include),tolerance)
dd=range(1,14,3)

print "a",aa,"b",bb,"c",cc,"d",dd
print 4 in aa #return ture/false
print 3 not in bb
print "c+d",cc+dd
print bb*3
print dd[1:10:2] #extract value 1~10 as steps 2
print cc.index(8) # cc.index(x,i,j)
print "'b' in a",aa.count('b') # count the times 'b' shows

aa[4]='great' #can change
aa[1:3]=[10,20,30] # replace
print "a",aa
del aa[4:5] # delete from 4, stop at 5(5 is not be deleted)
print "a",aa
cc.append(99) # cc+[99]
print "c",cc
dd.extend(cc) # dd+cc
print "d",dd
cc.insert(0,4) # insert 4 before 0
print "c",cc
aa.pop(3) #delete i element
print "a",aa
