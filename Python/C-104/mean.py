import csv


with open('HeightWeight.csv', newline='') as f:
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