# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:31:42 2022
Convert Openvibe Markers to any other (read from Dict.txt)

@author: P154492, M.M.Span
"""

# importing the module
import csv
import glob
import os
  
# reading the data from the file
with open('Dict.txt') as f:
    reader = csv.reader(f)
    mydict = {}
    for rows in reader:
        k,v = rows
        mydict[k] = v
path = '.'
filenames = glob.glob(path + "\*.vmrk")
for filename in filenames:
    print(filename)
    with open(filename) as f:
        lines = f.readlines()
        newlines = []
        for line in lines:
            if line.find("Mk") == -1: # Any line not containing markers is copied verbatim
                newlines.append(line)
            else:
                thisline = False
                for key in mydict.keys(): # Check for each of the markers, if it is found, copy it
                    if line.find(key) != -1:
                        newlines.append(line.replace(key, mydict[key]))
                        thisline = True
                        break
                if not thisline: # no key found in the Markerline: just copy it varbatim
                    newlines.append(line)
                    
        f.close()
    #os.rename(filename, "old/" + filename)
    with open(filename, 'w') as f:
        f.writelines(newlines)
        f.close()
    