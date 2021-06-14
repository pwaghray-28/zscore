import random
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
import pandas as pd
data = pd.read_csv("studentMarks.csv")
data1 = data["Math_score"].tolist()
graph = ff.create_distplot([data1],["Math_score"])
graph.show()
mean  = statistics.mean(data1)
standarddeviation = statistics.stdev(data1)
def samplingmean():
    data = []
    for i in range(100):
        randomindex = random.randint(0,len(data1)-1)
        value = data1[randomindex]
        data.append(value)
    mean = statistics.mean(data)
    return mean
meanlist = []
for i in range (1000):
    tmean = samplingmean()
    meanlist.append(tmean)
graph = ff.create_distplot([meanlist],["Math_score"])
graph.show()