def print_none():
    print "Hello World!" # 4 retract
def print_one(arg):
    print "I like %s."%arg
def print_two(arg1,arg2):
    print "I hate %s and %s"%(arg1,arg2)

print_none()
likes=raw_input("Input what you like: ")
print_one(likes)
diss1,diss2=raw_input("Input 2 of what you dislike: ").split() # raw_input more than one argument!
print_two(diss1,diss2)

def add(a,b):
    return a+b
groupA=20
groupB=30
total=add(groupA,groupB)
print "Total is %d."%total
