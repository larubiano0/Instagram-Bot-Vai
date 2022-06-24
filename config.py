import os

directory = 'csvdata'

data = {}

for file in os.listdir(directory): #For each filename in the directory
    path = os.path.join(directory, file) #corpus/python.txt
    file = file[:-4] #Removes .csv
    data[file] = path            

iglogin = {}

with open('iglogin.env') as f:

    for line in f:

        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)

        iglogin[key] = value