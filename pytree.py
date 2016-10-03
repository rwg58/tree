#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here
if len(sys.argv) == 1:  
    currentPath = os.getcwd()  
else:  
    currentPath = sys.argv[1]  

def filetree(path, t, has):  
    has.append(True)  
    block = '  '  
    for i in range(t):  
        if has[i] == True: block += '|  '  
        else: block += '   '  
    dirs = os.listdir(path)  
    for i in dirs:  
        tmp = path + os.sep + i  
        if i == dirs[-1]:  
            down = '|-'  
            has[t] = False  
        else:  
            down = '|-'  
            has[t] = True  
        print (block + down + i)  
        if os.path.isdir(tmp) :  
            filetree(tmp, t + 1, has)  

#print (currentPath)  
#filetree(currentPath, 0, [])  


if __name__ == '__main__':
    # just for demo
#    subprocess.run(['tree'] + sys.argv[1:])
    print (currentPath)  
    filetree(currentPath, 0, []) 
