#!/usr/bin/env python3
import subprocess
import sys
import os
import re
from os import listdir, sep, walk
from os.path import abspath, basename, isdir


def clean_hidden_files(list):
    newdirs = [item for item in list if item[0] != '.']
    return newdirs


def filetree(path, t, has):
    has.append(True)
    block = ''
    for i in range(t):
        if has[i] is True:
            block = block + '│   '
        else:
            block = block + '    '
    dirs = os.listdir(path)
    dirs = clean_hidden_files(dirs)
    dirs = sorted(dirs, key=lambda x: re.sub('[^a-zA-Z0-9]+', '', x).lower())
    for i in dirs:
        tmp = path + os.sep + i
        if i == dirs[-1]:
            down = '└── '
            has[t] = False
        else:
            down = '├── '
            has[t] = True
        print(block + down + i)
        if os.path.isdir(tmp):
            filetree(tmp, t + 1, has)


def count_em(valid_path):
    dir_count = 0
    file_count = 0
    for root, dirs, files in os.walk(valid_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        dir_count += len(dirs)

        for f in files:
            if not f.startswith('.'):
                file_count += 1
    print(dir_count, "directories,", file_count, "files")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('.')
        currentPath = os.getcwd()
    else:
        currentPath = sys.argv[1]
        print(currentPath)
    filetree(currentPath, 0, [])
    print('')
    count_em(currentPath)
