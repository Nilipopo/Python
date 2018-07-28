sa={1,2,3,'a','b','c'}
da={'qrrrr':1003,'cjnn':'npercent','user222':'0805nl',(1,2,3):'cba',4563:9875}

print sa,'\n',da,da['qrrrr']

del da[4563] # dicts delete
print da

da['xixi']=666 # dicts add
print da

sa.add(5) # sets add
sa.remove('a') # sets remove
sa.discard('b') # sets delete
sa.discard('dd') # try delete an nonexistent element ~~~~~ not report an error!
sa.remove('d') ## error!!!
print sa,'\t'
