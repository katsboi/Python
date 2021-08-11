import csv


with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))

new_data.sort()
n = len(new_data) 

if n % 2 != 0:
    median = new_data[n//2]
else:
    median = (float(new_data[n//2])+float(new_data[n//2  + 1]))/2

print("The Median is: " + str(median))