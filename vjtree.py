# implement the tree command in python
# basic idea: tree(path)
# - Go to path, for each file in path, check if the file is a dir
# - if it is a dir, call tree(file) recursively else print the name of the file


import sys
import os

# usage: $ vjtree.py <dir>

def vjtree(vjpath):
    #print "Dir listing: ",
    #print os.listdir(vjpath)
    for f in os.listdir(vjpath):
        pathname = os.path.join(vjpath, f)
        if os.path.isdir(pathname):
            print "Dir: %s" %(pathname)
            vjtree(pathname)
        else:
            print "\tFile: %s" %(pathname)



if __name__ == '__main__':
    vjtree(sys.argv[1])
