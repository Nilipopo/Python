from sys import argv
script,textfile=argv
text=open(textfile,'w') # 'w'~write,'a'~add,'r'~read,'w+'~write & read,'a+'~add & read

line1="My name is CZNN."
line2="I like singing and dancing."

text.write(line1)
text.write("\n") # newline
text.write(line2)
text.write("\n")
text.close() #!
