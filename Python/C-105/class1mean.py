import csv


with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))
    
sum = 0

for i in new_data:
   sum = i + sum

avg = sum/len(new_data)

print("Mean / Average is: " + str(avg))


import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= avg, y1= avg,
      x0= 0, x1= len(new_data)
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()

