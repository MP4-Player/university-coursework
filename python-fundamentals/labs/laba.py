# -*- coding: utf-8 -   *-
import random
import string
import os
import sys

def CountF(fname):
    N = 0
    try:
        with open(fname,'r') as f:
            for line in f:
                N += 1
                #print(N,":",line)
    except IOError:
        return -1
    finally:
        return N

file1 = "text17_1.txt"
file2 = "text17_2.txt"
print("Read from:",file1)
print("Read from:",file2)

N1 = CountF(file1)
N2 = CountF(file2)

print("N1:",N1)
print("N2:",N2)

try:
    #file for temporary data
    N = random.randrange(5,8)
    S = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase \
        + string.digits) for _ in range(N))
    temp_file = "temp_" + S + ".txt"
    #print()
    print("Temp file:",temp_file)

    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(temp_file, 'w') as outfile:
        if N1 <= N2:
            for x, y in zip(f1, f2):
                #print("{0} : {1}".format(x.strip(), y.strip()))
                outfile.write("{0} : {1}".format(x.strip(), y))
        else:
            for i in range(0,N2):
                x = f1.readline()
                y = f2.readline()
                outfile.write("{0} : {1}\n".format(x.strip(), y.strip()))
            for i in range(N2,N1):
                x = f1.readline()
                outfile.write(x)

    with open(file1, 'w') as outfile, open(temp_file, 'r') as infile:
        for line in infile:
            outfile.write(line)

    #sys.exit()

    try:
        os.remove(temp_file)
    except OSError as e:
        print("\nError:", e)

except IOError:
    print('Open error: ',file1)