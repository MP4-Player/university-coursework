ishodnik= open('test50000.txt')
nechot=open('myFile.txt','w')
chot=open('myFile2.txt','w')
for index, data in enumerate(ishodnik.readlines()):
    if index % 2 == 0:
        nechot.write(data)
    else:
        chot.write(data)
ishodnik.close()
nechot.close()
chot.close()