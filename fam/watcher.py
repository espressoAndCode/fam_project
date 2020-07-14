import os

flist = []

def traverse(topdir):
    for root, dnames, fnames in os.walk(topdir):
        for f in fnames:
            flist.append(os.path.join(root, f))

            
