import csv
import math

dir_file = "2_1_System/"
file_nam = "trial1_run"

alpha = -1
service = 1.68333333334

grand_average = []
grand_ratio = []
average_var = 0
ratio_var = 0

for i in range(1000):
    max_time = 0
    average = 0
    ratio = 0
    var = 0
    data = open(dir_file + file_nam + str(i) + ".csv")
    csv_reader = csv.reader(data, delimiter='\t')
    line_count = 0
    count = 0
    for row in csv_reader:
        if row[0][0] == 'S':
            break
        if line_count == 0:
            line_count += 1
            continue
        if float(row[4]) > 30:
            continue
        average += float(row[4]) + alpha * (float(row[3]) - service)
        max_time = float(row[0])
        ratio = float(row[5])
        count += 1
    average /= count
    data.seek(0)
    line_count = 0
    #for row in csv_reader:
    #    if row[0][0] == 'S':
    #        break
    #    if line_count == 0:
    #        line_count += 1
    #        continue
    #    var += (float(row[4]) - (average))**2
    #var /= (count - 1)
    grand_average.append(average)
    grand_ratio.append(ratio/max_time)

calculated_average = (sum(grand_average)/1000)
print(calculated_average)
for i in grand_average:
    average_var += (i - calculated_average)**2
average_var /= 999
print(average_var)
print()
calculated_ratio = sum(grand_ratio)/1000
print(calculated_ratio)
for i in grand_ratio:
    ratio_var += (i - calculated_ratio)**2
ratio_var /= 999
print(ratio_var)
