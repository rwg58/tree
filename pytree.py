#!/usr/bin/env python3
import subprocess
import sys
import os
import re


def clean_hidden_files(list):
    newdirs = [item for item in list if item[0] != '.']
    newfiles = sorted(newdirs, key=lambda x: re.sub('[^a-zA-Z0-9]+', '', x).lower())
    return newfiles


def filetree(path, t, has):
    has.append(True)
    block = '  '
    for i in range(t):
        if has[i] is True:
            block = block + '│  '
        else:
            block = block + '   '
    dirs = os.listdir(path)
    dirs = clean_hidden_files(dirs)
    for i in dirs:
        tmp = path + os.sep + i
        if i == dirs[-1]:
            down = '└──'
            has[t] = False
        else:
            down = '├──'
            has[t] = True
        print(block + down + i)
        if os.path.isdir(tmp):
            filetree(tmp, t + 1, has)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        currentPath = os.getcwd()
    else:
        currentPath = sys.argv[1]
    print(currentPath)
    filetree(currentPath, 0, []) 
