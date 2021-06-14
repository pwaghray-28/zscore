import random
import plotly.express as px
import plotly.figure_factory as ff 
import statistics
count = []
dice = []
for i in range (0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice.append(dice1+dice2)
    count.append(i)
graph = px.bar(x = dice,y = count)
graph2 = ff.create_distplot([dice],["dice results"])
#graph.show()
#graph2.show()
print("done")
mean = statistics.mean(dice)
standarddeviation = statistics.stdev(dice)
print(mean,standarddeviation)
median = statistics.median(dice)
mode = statistics.mode(dice)
print(mode, median)
firstsdstart,firstsdend = mean-standarddeviation,mean+standarddeviation
secondsdstart,secondsdend = mean-2*standarddeviation,mean+2*standarddeviation
thirdsdstart,thirdsdend = mean-3*standarddeviation,mean+3*standarddeviation
firstsddata = [result for result in dice if result>firstsdstart and result<firstsdend]
print(len(firstsddata)/len(dice))
secondsddata = [result for result in dice if result>secondsdstart and result<secondsdend]
print(len(secondsddata)/len(dice))
thirdsddata = [result for result in dice if result>thirdsdstart and result<thirdsdend]
print(len(thirdsddata)/len(dice))