from sys import argv
script,textfile=argv
text=open(textfile)
print "The content of %s:\n"%textfile
print text.read()
