import sys
import os
import pandas
import random

def manipulate_file():
    lines = []
    file_name = '.\\sample.txt'
    if (len(sys.argv) > 1):
        file_name = sys.argv[1]
    # print(os.listdir())
    fi = open(file_name, mode='r')
    lines = fi.readlines()
    fi.close()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].lower() # cHANGE string to lower case
    print(lines)
    lines.sort()
    fo = open('output.txt', mode='w')
    fo.write('\n'.join(lines))
    fo.close()
    n = random.randint(0,6)
    print(n)

    lines.remove(lines[1])
    lines.pop(2)
    lines.append('abc')
    
    dict = {'c': 3, 'd': 4}
    dict['a'] = 1
    dict['b'] = 2
    print(list(dict.keys()))
    dict.pop('a')
    print(dict)



manipulate_file()