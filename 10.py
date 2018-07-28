def print_none():
    print "Hello World!" # 4 retract
def print_one(arg):
    print "I like %s."%arg
def print_two(arg1,arg2):
    print "I hate %s and %s"%(arg1,arg2)

print_none()
likes=raw_input("Input what you like: ")
print_one(likes)
print_two("hot weather","tart flavour")

def add(a,b):
    return a+b
groupA=20
groupB=30
total=add(groupA,groupB)
print "Total is %d."%total
