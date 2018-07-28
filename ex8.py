textfile=raw_input("Input the textfile:\n")
text=open(textfile)
print "The content of %s:\n"%textfile
print text.read()
