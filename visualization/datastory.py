import random
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import pandas as pd
data = pd.read_csv("data1.csv")
data1 = data["average"].tolist()
graph = ff.create_distplot([data1],["average"])
graph.show()
mean = statistics.mean(data1)
sd = statistics.stdev(data1)
def randomset():
dataset = []
for i in range(0,100):
    index = random.randint(0,len(data1))
    value = data[index]
    dataset.append(value)
    samplemean = statistics.mean(dataset)
    return samplemean