from sys import argv
script,textfile1,textfile2=argv
text1=open(textfile1)
text2=open(textfile2,'a+')

t=text1.read()
text2.write(t)
text2.seek(0) # 0~start(Or stay at the end and read nothing)

print text2.read()
