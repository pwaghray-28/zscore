import csv
with open("path1.csv")as f:
    reader = csv.ready(f)
    data = list(reader)
data.pop(0)
total = 0
totalentries = len(data)
for marks in data:
    total = total+float(marks[1])
mean = total/totalentries
import pandas as p 
import plotly.express as px
df = pd.read_csv("class1.csv")
figure = px.scatter(df,x = "Student Number", y = "Marks")
figure.update_layout(shapes = [dict(type = 'line',y0 = mean, y1 = mean, x0 = 0, x1 = totalentries)])
figure.show()