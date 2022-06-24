import os
import sys

directory = 'csvdata'

data = {}

for file in os.listdir(directory): #For each filename in the directory
    path = os.path.join(directory, file) #corpus/python.txt
    file = file[:-4] #Removes .csv
    data[file] = path             