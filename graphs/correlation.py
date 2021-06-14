import csv 
import numpy as mp
def getdata(path):
    var1 = []
    var2 = []
    with open(path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            var1.append(float(row["Size of TV"])) 
            var2.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    correlation = mp.corrcoef(var1,var2)
    print(correlation)
getdata("TV.csv") 
