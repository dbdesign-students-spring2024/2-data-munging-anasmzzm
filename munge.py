data_file = open('data\GLB.Ts+dSST.txt', 'r')
data_lines = data_file.readlines()

csv_file = list()
csv_file_format = list()

counter = 0
for i in range(len(data_lines)):
    if 'Year' in data_lines[i]:
        break
    if 'Year' in data_lines[i]:
        counter += 1
csv_file.append(data_lines[counter]) 

for i in range(counter, len(data_lines)): 
    if 'Divide' in data_lines[i]: 
        break 
    if "Year" not in data_lines[i]:
        csv_file.append(data_lines[i]) 

for i in range(len(csv_file)): 
    csv_file[i] = csv_file[i].strip('\n')

while '' in csv_file:
    csv_file.remove('')

for i in range(len(csv_file)):
    for k in range(len(csv_file[i].split(' '))):
        csv_file_format.append(csv_file[i].split(' ')[k])

data_file.close() 

for num in range(len(csv_file_format)):
    if csv_file_format[num] == '****':
        total = int(csv_file_format[num-3]) + int(csv_file_format[num-13]) + int(csv_file_format[num-14])
        DJF_average = int(total / 3)
        csv_file_format[num] = DJF_average
        
    if csv_file_format[num] == '***':
        total = int(csv_file_format[num-2]) + int(csv_file_format[num - 3])
        DN_average = total / 2
        csv_file_format[num] = int(DN_average)

counter = 0
for k in range(20, len(csv_file_format)):
    if(len(str(csv_file_format[k])) != 4):
        csv_file_format[k] = format((int(csv_file_format[k])/ 100) * 1.8, '.1f')

csv_file_created = open("clean_data.csv", "w")
for i in range(0, len(csv_file_format), 20):
    line = ','.join(map(str, csv_file_format[i:i+14]))
    csv_file_created.write(line + '\n')

csv_file_created.close()    
