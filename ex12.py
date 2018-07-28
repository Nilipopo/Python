aa=[1,2,3,'a','b','c']
bb=(1,2,3,'a','b','c')
cc=range(0,10,2)
dd=range(1,14,3)

print aa," ",bb," ",cc," ",dd
print 4 in aa
print 3 not in bb
print cc+dd
print bb*3
print dd[1:10:2]
print cc.index(8) # cc.index(x,i,j)
print aa.count('b')

aa[4]='great'
aa[1:3]=[10,20,30]
print aa
del aa[4:5]
print aa
