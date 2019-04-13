import os

# Number of trial
num = 1000

# File path for batch file
trial = "3_1_Sim"
path = "../" + trial + "/" + str(num) + "/BLAZE.exp"

# Open file
file_object = open(path, "w")

# Print line for individual trials
for i in range(num):
    file_object.write(trial + "_run_" + str(i) + ".csv   n   " + str(i+1) + "  240  1\n")

# Close file
file_object.close()
