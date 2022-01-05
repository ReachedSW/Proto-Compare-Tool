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

try:
    itemlistFile = open("item_list.txt", "r")
except:
    print("File is not in this folder !")
    os.system("PAUSE")
    sys.exit()

itemlist = []
for idx in itemlistFile.readlines():
    itemlist.append(idx.split("\t")[0]) # append itemlist's numbers trough to list



with open("missing_itemnames.txt", "w", encoding='UTF-8') as missing_vnums: #Those in itemnames but not in itemproto and itemlist
    for i in itemnames:
        if i == "VNUM":
            continue
        if "~" in i:
            continue
        if i not in itemproto:
            missing_vnums.writelines("Item proto dosyasında %d eksik" % int(i) + "\n")
        elif i not in itemlist:
            missing_vnums.writelines("Item list dosyasında %d eksik" % int(i) + "\n")
        else:
            continue

with open("missing_itemproto.txt", "w", encoding='UTF-8') as missing_vnums:
    for j in itemproto:
        if j == "Vnum":
            continue
        if "~" in j:
            continue
        if j not in itemnames:
            missing_vnums.writelines("Item anmes dosyasında %d eksik" % int(j) + "\n")
        elif j not in itemlist:
            missing_vnums.writelines("Item list dosyasında %d eksik" % int(j) + "\n")
        else:
            continue

with open("missing_itemlist.txt", "w", encoding='UTF-8') as missing_vnums:
    for k in itemlist:
        if k not in itemnames:
            missing_vnums.writelines("Item names dosyasında %d eksik" % int(k) + "\n")
        elif k not in itemproto:
            missing_vnums.writelines("Item Proto dosyasında %d eksik" % int(k) + "\n")
        else:
            continue