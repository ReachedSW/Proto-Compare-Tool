#Author : Reached
#Date : 08.11.2021

import os
import sys

try:
    file = open("item_names.txt", "r")
except:
    print("File is not in this folder !")
    os.system("PAUSE")
    sys.exit()

mylist = []

mylist = file.readlines()
itemnames = [] # itemnames's vnum.
for index in mylist:
    itemnames.append(index.split("\t")[0])# append itemnames's numbers trough to list


try:
    protofile = open("item_proto.txt", "r")
except:
    print("File is not in this folder !")
    os.system("PAUSE")
    sys.exit()
protolist = []
protolist = protofile.readlines()

itemproto = []
for idx in protolist:
    itemproto.append(idx.split("\t")[0]) # append itemproto's numbers trough to list



# and now compare this 2 list

for i in itemnames:
    if i not in itemproto:
        print("Item proto dosyasında %d eksik" % int(i))
    else:
        continue

for j in itemproto:
    if j not in itemnames:
        print("Item names dosyasında %d eksik" % int(j))