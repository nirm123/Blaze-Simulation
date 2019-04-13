import csv
import math

# Number of trials
num = 1000

# Which sigma model
version = "2_1_Sim"

# Complete filepath/filename
dir_file = "../" + str(version) + "/" + str(num) + "/"
file_nam = version + "_run_"

# Alpha/Mean for variance reduction with control variates 
alpha = -1
service = 1.68333333334

# Averages of sojourn time for each trial
grand_average = []

# Ratio of time queue 0 is longer than 4 for each trial
grand_ratio4 = []

# Ratio of time queue 0 is longet than 8 for each trial
grand_ratio8 = []

# Calculated variance for average soujourn time and ratios 
average_var = 0
ratio_var4 = 0
ratio_var8 = 0

# Iterate through all trials
for i in range(num):
    # Variable for finishing time of trial
    max_time = 0

    # Accumulator for average
    average = 0
    
    # Variable for ratio 4
    ratio4 = 0

    # Variable for ratio 8
    ratio8 = 0

    # Open csv file
    data = open(dir_file + file_nam + str(i) + ".csv")
    
    # Set up csv reader
    csv_reader = csv.reader(data, delimiter='\t')
    
    # Variable to ignor first row
    line_count = 0

    # Variable to keep count of the number of customers
    count = 0

    # Iterate through each customer for stats
    for row in csv_reader:
        # Final row
        if row[0][0] == 'S':
            break

        # Ignore the first row
        if line_count == 0:
            line_count += 1
            continue

        # Ignore customers with sojourn time longer than 35 (error in simulation)
        if float(row[4]) > 30:
            continue

        # Running sum for average
        average += float(row[4]) + alpha * (float(row[3]) - service)

        # Update max_time
        max_time = float(row[0])
        
        # Update ratio8 time
        ratio8 = float(row[5])
        
        # Update ratio4 time
        ratio4 = float(row[6])

        # Keep count of number of customers
        count += 1

    # Calculate average
    average /= count
    
    # Append average, ratio4, and ratio8
    grand_average.append(average)
    grand_ratio4.append(ratio4/max_time)
    grand_ratio8.append(ratio8/max_time)

# Calculated average sojourn time
calculated_average = (sum(grand_average)/num)
print(calculated_average)

# Calculate variance of sojourn time
for i in grand_average:
    average_var += (i - calculated_average)**2
average_var /= (num - 1)
print(average_var)
print()

# Calculated ratio of time with line greater than 4
calculated_ratio4 = sum(grand_ratio4)/num
print(calculated_ratio4)

# Calculate variance of time with line greater than 4
for i in grand_ratio4:
    ratio_var4 += (i - calculated_ratio4)**2
ratio_var4 /= (num - 1)
print(ratio_var4)
print()

# Calculated ratio of time with line greater than 8
calculated_ratio8 = sum(grand_ratio8)/num
print(calculated_ratio8)

# Calculate variance of time with line greater than 8
for i in grand_ratio8:
    ratio_var8 += (i - calculated_ratio8)**2
ratio_var8 /= (num - 1)
print(ratio_var8)
