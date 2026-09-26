inp= open('file.txt')
out1=open('1file.txt','w')
out2=open('2file.txt','w')
for index, data in enumerate(inp.readlines()):
    if index % 2 == 0:
        out1.write(data)
    else:
        out2.write(data)
inp.close()
out1.close()
out2.close()

