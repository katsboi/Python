import csv
import math

with open('class2.csv', newline='') as f:
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

mean = sum/len(new_data)

print("Mean / Average is: " + str(mean))

squaredList= []

for i in new_data:
    sub = i - mean
    square=sub**2
    squaredList.append(square)

sum =0
for i in squaredList:
    sum =sum + i

result = sum/ (len(new_data)-1)

std_deviation = math.sqrt(result)
print("standard deviation is= ",std_deviation)