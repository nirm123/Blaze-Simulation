import pandas as pd
import datetime
import time
import scipy.stats as ss

# Format for duration data
format = '%M:%S:%f'

# Load csv
sheet = pd.read_csv("../Data/Blaze_stats.csv")

# Open file to write results
f = open("../Data/chi_squared.txt","w") 

# List of columns (different dataets that we want to find a distribution to model)
col = ["Interarrival (B)", "Interarrival (I)", "Toppings", "Cooking", "Finishing"]

# List to store calculated statistics
data = [[None for _ in range(30)] for _ in range(5)]
stat = [[None for _ in range(4)] for _ in range(5)]
count = 0

# Iterate through columns in csv
for i in col:
    # Keep track of min and max times for columns
    cur_min = sheet[i].min()
    cur_max = sheet[i].max()

    # Convert duration into minutes and store in list
    for j in range(30):
        x = time.strptime(sheet[i][j], format)
        data[count][j] = (datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()/60)
        if cur_min == sheet[i][j]:
            stat[count][0] = data[count][j]
        if cur_max == sheet[i][j]:
            stat[count][1] = data[count][j]

    # Calculate delta between min and max
    stat[count][2] = stat[count][1] - stat[count][0]
    count += 1

# Set of data we want to check against exponential
exp_set = [0, 1, 4];

# Chi squared test between data and exponential
for i in exp_set:
    # Calculate average of data
    stat[i][3] = (sum(data[i])/30)

    # Calculate buckets to count obsercations
    buc5 = 3*stat[i][3]
    buc1 = buc5/5
    buc2 = buc1 * 2
    buc3 = buc1 * 3
    buc4 = buc1 * 4

    # Calculated expected number of observations in each bucket
    e1 = ss.expon.cdf(buc1, 0, stat[i][3])
    e2 = ss.expon.cdf(buc2, 0, stat[i][3])
    e3 = ss.expon.cdf(buc3, 0, stat[i][3])
    e4 = ss.expon.cdf(buc4, 0, stat[i][3])
    e5 = ss.expon.cdf(buc5, 0, stat[i][3])
    e6 = ((1 - e5) * 30)
    e5 = ((e5 - e4) * 30)
    e4 = ((e4 - e3) * 30)
    e3 = ((e3 - e2) * 30)
    e2 = ((e2 - e1) * 30)
    e1 = (e1 * 30)

    # Count for each bucket
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0

    # Chi squared variable
    X = 0

    # Assign each observation to bucket
    for j in range(30):
        if data[i][j] < buc1:
            c1 += 1
        elif data[i][j] < buc2:
            c2 += 1
        elif data[i][j] < buc3:
            c3 += 1
        elif data[i][j] < buc4:
            c4 += 1
        elif data[i][j] < buc5:
            c5 += 1
        else:
            c6 += 1

    # Calculate chi squared test statistic
    X += (c1 - e1)**2/(e1)
    X += (c2 - e2)**2/(e2)
    X += (c3 - e3)**2/(e3)
    X += (c4 - e4)**2/(e4)
    X += (c5 - e5)**2/(e5)
    X += (c6 - e6)**2/(e6)

    # Output results
    if i == 0:
        f.write("X^2 (5 dof) of Interarrival (B) being exp(" + str(stat[i][3]) + "): " + str(X) + "\n\n")
    elif i == 4:
        f.write("X^2 (5 dof) of Finishing being exp(" + str(stat[i][3]) + "): " + str(X) + "\n\n")
    else:
        f.write("X^2 (5 dof) of Interarrival (I) being exp(" + str(stat[i][3]) + "): " + str(X) + "\n\n")

# Chi squared test between data and uniform
for i in range(2, 4):
    # Expected number in each bucket
    expected = 5

    # Calculate buckets
    buc1 = stat[i][0] + stat[i][2]/6
    buc2 = stat[i][0] + 2*stat[i][2]/6
    buc3 = stat[i][0] + 3*stat[i][2]/6
    buc4 = stat[i][0] + 4*stat[i][2]/6
    buc5 = stat[i][0] + 5*stat[i][2]/6

    # Variables to store number of observations in each bucket
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0

    # Variable for chi squared
    X = 0

    # Assign each observation to bucket
    for j in range(30):
        if data[i][j] < buc1:
            c1 += 1
        elif data[i][j] < buc2:
            c2 += 1
        elif data[i][j] < buc3:
            c3 += 1
        elif data[i][j] < buc4:
            c4 += 1
        elif data[i][j] < buc5:
            c5 += 1
        else:
            c6 += 1

    # Calculate chi squared test statistic
    X += (c1-expected)**2/expected
    X += (c2-expected)**2/expected
    X += (c3-expected)**2/expected
    X += (c4-expected)**2/expected
    X += (c5-expected)**2/expected
    X += (c6-expected)**2/expected

    # Output results
    if i == 2:
        f.write("X^2 (5 dof) of Toppings being U(" + str(stat[i][0]) + ", " + str(stat[i][1]) + "): " + str(X) + "\n\n")
    else:
        f.write("X^2 (5 dof) of Cooking being U(" + str(stat[i][0]) + ", " + str(stat[i][1]) + "): " + str(X))

# Close file
f.close()
