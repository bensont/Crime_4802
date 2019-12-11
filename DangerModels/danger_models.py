# This calculates the dangers for each area and for a model and outputs to a file
# to allow for regression calculations

import csv

# Create lists to hold needed attributes
areaID = []
severity = []
crimeType = []

# Three sets of read write, different uses

# Get dangers for a single model to linreg
# read_file = "training_model_5.csv"
# write_file = "dangers_model_5.csv"

# Get splits to compare diff dangers against (do both a and b)
# read_file = "training_splita.csv"
# write_file = "dangers_model_5_splita.csv"

# Final model test
read_file = "clean_best_training.csv"
write_file = "best_training_dangers.csv"

# Read the file and insert each value into the correct list
with open(read_file,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # All weighting, categorizing, and classing is done per line to reduce runtime
    for line in csv_reader:
        current_A = int(line[0])
        current_S = float(line[1])
        current_C = int(line[2])
        areaID.append(current_A)
        severity.append(current_S)
        crimeType.append(current_C)

# Find the total crimes in the data
total_crimes = len(areaID)
all_info = [areaID,severity,crimeType]

# List for the total crimes per area
t_per_area = [0]*21

# List of areas with lists of types of crime in that area
numC_area = [[0]*6]*21

# Assigning severity
sev1 = 0.0000147687
sev2 = 0.004328296
sev3 = 0.016911184
sev4 = 0.000304396
sev5 = 0.000945535
sev6 = 0.013554454


# Totals for each crime given each area
# Area 1
c1_a1 = 0
c2_a1 = 0
c3_a1 = 0
c4_a1 = 0
c5_a1 = 0
c6_a1 = 0
# Area 2
c1_a2 = 0
c2_a2 = 0
c3_a2 = 0
c4_a2 = 0
c5_a2 = 0
c6_a2 = 0
# Area 3
c1_a3 = 0
c2_a3 = 0
c3_a3 = 0
c4_a3 = 0
c5_a3 = 0
c6_a3 = 0
# Area 4
c1_a4 = 0
c2_a4 = 0
c3_a4 = 0
c4_a4 = 0
c5_a4 = 0
c6_a4 = 0
# Area 5
c1_a5 = 0
c2_a5 = 0
c3_a5 = 0
c4_a5 = 0
c5_a5 = 0
c6_a5 = 0
# Area 6
c1_a6 = 0
c2_a6 = 0
c3_a6 = 0
c4_a6 = 0
c5_a6 = 0
c6_a6 = 0
# Area 7
c1_a7 = 0
c2_a7 = 0
c3_a7 = 0
c4_a7 = 0
c5_a7 = 0
c6_a7 = 0
# Area 8
c1_a8 = 0
c2_a8 = 0
c3_a8 = 0
c4_a8 = 0
c5_a8 = 0
c6_a8 = 0
# Area 9
c1_a9 = 0
c2_a9 = 0
c3_a9 = 0
c4_a9 = 0
c5_a9 = 0
c6_a9 = 0
# Area 10
c1_a10 = 0
c2_a10 = 0
c3_a10 = 0
c4_a10 = 0
c5_a10 = 0
c6_a10 = 0
# Area 11
c1_a11 = 0
c2_a11 = 0
c3_a11 = 0
c4_a11 = 0
c5_a11 = 0
c6_a11 = 0
# Area 12
c1_a12 = 0
c2_a12 = 0
c3_a12 = 0
c4_a12 = 0
c5_a12 = 0
c6_a12 = 0
# Area 13
c1_a13 = 0
c2_a13 = 0
c3_a13 = 0
c4_a13 = 0
c5_a13 = 0
c6_a13 = 0
# Area 14
c1_a14 = 0
c2_a14 = 0
c3_a14 = 0
c4_a14 = 0
c5_a14 = 0
c6_a14 = 0
# Area 15
c1_a15 = 0
c2_a15 = 0
c3_a15 = 0
c4_a15 = 0
c5_a15 = 0
c6_a15 = 0
# Area 16
c1_a16 = 0
c2_a16 = 0
c3_a16 = 0
c4_a16 = 0
c5_a16 = 0
c6_a16 = 0
# Area 17
c1_a17 = 0
c2_a17 = 0
c3_a17 = 0
c4_a17 = 0
c5_a17 = 0
c6_a17 = 0
# Area 18
c1_a18 = 0
c2_a18 = 0
c3_a18 = 0
c4_a18 = 0
c5_a18 = 0
c6_a18 = 0
# Area 19
c1_a19 = 0
c2_a19 = 0
c3_a19 = 0
c4_a19 = 0
c5_a19 = 0
c6_a19 = 0
# Area 20
c1_a20 = 0
c2_a20 = 0
c3_a20 = 0
c4_a20 = 0
c5_a20 = 0
c6_a20 = 0
# Area 20
c1_a21 = 0
c2_a21 = 0
c3_a21 = 0
c4_a21 = 0
c5_a21 = 0
c6_a21 = 0
# Find the totals for each area
for idx in range(len(areaID)):
    # area 1
    if (areaID[idx] == 1):
        t_per_area[0] += 1
        if (crimeType[idx]) == 1:
            c1_a1 += 1
        elif (crimeType[idx]) == 2:
            c2_a1 += 1
        elif (crimeType[idx]) == 3:
            c3_a1 += 1
        elif (crimeType[idx]) == 4:
            c4_a1 += 1
        elif (crimeType[idx]) == 5:
            c5_a1 += 1
        elif (crimeType[idx]) == 6:
            c6_a1 += 1
    elif (areaID[idx] == 2):
        t_per_area[1] += 1
        if (crimeType[idx]) == 1:
            c1_a2 += 1
        elif (crimeType[idx]) == 2:
            c2_a2 += 1
        elif (crimeType[idx]) == 3:
            c3_a2 += 1
        elif (crimeType[idx]) == 4:
            c4_a2 += 1
        elif (crimeType[idx]) == 5:
            c5_a2 += 1
        elif (crimeType[idx]) == 6:
            c6_a2 += 1
    elif (areaID[idx] == 3):
        t_per_area[2] += 1
        if (crimeType[idx]) == 1:
            c1_a3 += 1
        elif (crimeType[idx]) == 2:
            c2_a3 += 1
        elif (crimeType[idx]) == 3:
            c3_a3 += 1
        elif (crimeType[idx]) == 4:
            c4_a3 += 1
        elif (crimeType[idx]) == 5:
            c5_a3 += 1
        elif (crimeType[idx]) == 6:
            c6_a3 += 1
    elif (areaID[idx] == 4):
        t_per_area[3] += 1
        if (crimeType[idx]) == 1:
            c1_a4 += 1
        elif (crimeType[idx]) == 2:
            c2_a4 += 1
        elif (crimeType[idx]) == 3:
            c3_a4 += 1
        elif (crimeType[idx]) == 4:
            c4_a4 += 1
        elif (crimeType[idx]) == 5:
            c5_a4 += 1
        elif (crimeType[idx]) == 6:
            c6_a4 += 1
    elif (areaID[idx] == 5):
        t_per_area[4] += 1
        if (crimeType[idx]) == 1:
            c1_a5 += 1
        elif (crimeType[idx]) == 2:
            c2_a5 += 1
        elif (crimeType[idx]) == 3:
            c3_a5 += 1
        elif (crimeType[idx]) == 4:
            c4_a5 += 1
        elif (crimeType[idx]) == 5:
            c5_a5 += 1
        elif (crimeType[idx]) == 6:
            c6_a5 += 1
    elif (areaID[idx] == 6):
        t_per_area[5] += 1
        if (crimeType[idx]) == 1:
            c1_a6 += 1
        elif (crimeType[idx]) == 2:
            c2_a6 += 1
        elif (crimeType[idx]) == 3:
            c3_a6 += 1
        elif (crimeType[idx]) == 4:
            c4_a6 += 1
        elif (crimeType[idx]) == 5:
            c5_a6 += 1
        elif (crimeType[idx]) == 6:
            c6_a6 += 1
    elif (areaID[idx] == 7):
        t_per_area[6] += 1
        if (crimeType[idx]) == 1:
            c1_a7 += 1
        elif (crimeType[idx]) == 2:
            c2_a7 += 1
        elif (crimeType[idx]) == 3:
            c3_a7 += 1
        elif (crimeType[idx]) == 4:
            c4_a7 += 1
        elif (crimeType[idx]) == 5:
            c5_a7 += 1
        elif (crimeType[idx]) == 6:
            c6_a7 += 1
    elif (areaID[idx] == 8):
        t_per_area[7] += 1
        if (crimeType[idx]) == 1:
            c1_a8 += 1
        elif (crimeType[idx]) == 2:
            c2_a8 += 1
        elif (crimeType[idx]) == 3:
            c3_a8 += 1
        elif (crimeType[idx]) == 4:
            c4_a8 += 1
        elif (crimeType[idx]) == 5:
            c5_a8 += 1
        elif (crimeType[idx]) == 6:
            c6_a8 += 1
    elif (areaID[idx] == 9):
        t_per_area[8] += 1
        if (crimeType[idx]) == 1:
            c1_a9 += 1
        elif (crimeType[idx]) == 2:
            c2_a9 += 1
        elif (crimeType[idx]) == 3:
            c3_a9 += 1
        elif (crimeType[idx]) == 4:
            c4_a9 += 1
        elif (crimeType[idx]) == 5:
            c5_a9 += 1
        elif (crimeType[idx]) == 6:
            c6_a9 += 1
    elif (areaID[idx] == 10):
        t_per_area[9] += 1
        if (crimeType[idx]) == 1:
            c1_a10 += 1
        elif (crimeType[idx]) == 2:
            c2_a10 += 1
        elif (crimeType[idx]) == 3:
            c3_a10 += 1
        elif (crimeType[idx]) == 4:
            c4_a10 += 1
        elif (crimeType[idx]) == 5:
            c5_a10 += 1
        elif (crimeType[idx]) == 6:
            c6_a10 += 1
    elif (areaID[idx] == 11):
        t_per_area[10] += 1
        if (crimeType[idx]) == 1:
            c1_a11 += 1
        elif (crimeType[idx]) == 2:
            c2_a11 += 1
        elif (crimeType[idx]) == 3:
            c3_a11 += 1
        elif (crimeType[idx]) == 4:
            c4_a11 += 1
        elif (crimeType[idx]) == 5:
            c5_a11 += 1
        elif (crimeType[idx]) == 6:
            c6_a11 += 1
    elif (areaID[idx] == 12):
        t_per_area[11] += 1
        if (crimeType[idx]) == 1:
            c1_a12 += 1
        elif (crimeType[idx]) == 2:
            c2_a12 += 1
        elif (crimeType[idx]) == 3:
            c3_a12 += 1
        elif (crimeType[idx]) == 4:
            c4_a12 += 1
        elif (crimeType[idx]) == 5:
            c5_a12 += 1
        elif (crimeType[idx]) == 6:
            c6_a12 += 1
    elif (areaID[idx] == 13):
        t_per_area[12] += 1
        if (crimeType[idx]) == 1:
            c1_a13 += 1
        elif (crimeType[idx]) == 2:
            c2_a13 += 1
        elif (crimeType[idx]) == 3:
            c3_a13 += 1
        elif (crimeType[idx]) == 4:
            c4_a13 += 1
        elif (crimeType[idx]) == 5:
            c5_a13 += 1
        elif (crimeType[idx]) == 6:
            c6_a13 += 1
    elif (areaID[idx] == 14):
        t_per_area[13] += 1
        if (crimeType[idx]) == 1:
            c1_a14 += 1
        elif (crimeType[idx]) == 2:
            c2_a14 += 1
        elif (crimeType[idx]) == 3:
            c3_a14 += 1
        elif (crimeType[idx]) == 4:
            c4_a14 += 1
        elif (crimeType[idx]) == 5:
            c5_a14 += 1
        elif (crimeType[idx]) == 6:
            c6_a14 += 1
    elif (areaID[idx] == 15):
        t_per_area[14] += 1
        if (crimeType[idx]) == 1:
            c1_a15 += 1
        elif (crimeType[idx]) == 2:
            c2_a15 += 1
        elif (crimeType[idx]) == 3:
            c3_a15 += 1
        elif (crimeType[idx]) == 4:
            c4_a15 += 1
        elif (crimeType[idx]) == 5:
            c5_a15 += 1
        elif (crimeType[idx]) == 6:
            c6_a15 += 1
    elif (areaID[idx] == 16):
        t_per_area[15] += 1
        if (crimeType[idx]) == 1:
            c1_a16 += 1
        elif (crimeType[idx]) == 2:
            c2_a16 += 1
        elif (crimeType[idx]) == 3:
            c3_a16 += 1
        elif (crimeType[idx]) == 4:
            c4_a16 += 1
        elif (crimeType[idx]) == 5:
            c5_a16 += 1
        elif (crimeType[idx]) == 6:
            c6_a16 += 1
    elif (areaID[idx] == 17):
        t_per_area[16] += 1
        if (crimeType[idx]) == 1:
            c1_a17 += 1
        elif (crimeType[idx]) == 2:
            c2_a17 += 1
        elif (crimeType[idx]) == 3:
            c3_a17 += 1
        elif (crimeType[idx]) == 4:
            c4_a17 += 1
        elif (crimeType[idx]) == 5:
            c5_a17 += 1
        elif (crimeType[idx]) == 6:
            c6_a17 += 1
    elif (areaID[idx] == 18):
        t_per_area[17] += 1
        if (crimeType[idx]) == 1:
            c1_a18 += 1
        elif (crimeType[idx]) == 2:
            c2_a18 += 1
        elif (crimeType[idx]) == 3:
            c3_a18 += 1
        elif (crimeType[idx]) == 4:
            c4_a18 += 1
        elif (crimeType[idx]) == 5:
            c5_a18 += 1
        elif (crimeType[idx]) == 6:
            c6_a18 += 1
    elif (areaID[idx] == 19):
        t_per_area[18] += 1
        if (crimeType[idx]) == 1:
            c1_a19 += 1
        elif (crimeType[idx]) == 2:
            c2_a19 += 1
        elif (crimeType[idx]) == 3:
            c3_a19 += 1
        elif (crimeType[idx]) == 4:
            c4_a19 += 1
        elif (crimeType[idx]) == 5:
            c5_a19 += 1
        elif (crimeType[idx]) == 6:
            c6_a19 += 1
    elif (areaID[idx] == 20):
        t_per_area[19] += 1
        if (crimeType[idx]) == 1:
            c1_a20 += 1
        elif (crimeType[idx]) == 2:
            c2_a20 += 1
        elif (crimeType[idx]) == 3:
            c3_a20 += 1
        elif (crimeType[idx]) == 4:
            c4_a20 += 1
        elif (crimeType[idx]) == 5:
            c5_a20 += 1
        elif (crimeType[idx]) == 6:
            c6_a20 += 1
    elif (areaID[idx] == 21):
        t_per_area[20] += 1
        if (crimeType[idx]) == 1:
            c1_a21 += 1
        elif (crimeType[idx]) == 2:
            c2_a21 += 1
        elif (crimeType[idx]) == 3:
            c3_a21 += 1
        elif (crimeType[idx]) == 4:
            c4_a21 += 1
        elif (crimeType[idx]) == 5:
            c5_a21 += 1
        elif (crimeType[idx]) == 6:
            c6_a21 += 1


# Totals for each crime given each area
# Area 1
p_c1_a1 = c1_a1 / t_per_area[0]
p_c2_a1 = c2_a1 / t_per_area[0]
p_c3_a1 = c3_a1 / t_per_area[0]
p_c4_a1 = c4_a1 / t_per_area[0]
p_c5_a1 = c5_a1 / t_per_area[0]
p_c6_a1 = c6_a1 / t_per_area[0]
# Area 2
p_c1_a2 = c1_a2 / t_per_area[1]
p_c2_a2 = c2_a2 / t_per_area[1]
p_c3_a2 = c3_a2 / t_per_area[1]
p_c4_a2 = c4_a2 / t_per_area[1]
p_c5_a2 = c5_a2 / t_per_area[1]
p_c6_a2 = c6_a2 / t_per_area[1]
# Area 3
p_c1_a3 = c1_a3 / t_per_area[2]
p_c2_a3 = c2_a3 / t_per_area[2]
p_c3_a3 = c3_a3 / t_per_area[2]
p_c4_a3 = c4_a3 / t_per_area[2]
p_c5_a3 = c5_a3 / t_per_area[2]
p_c6_a3 = c6_a3 / t_per_area[2]
# Area 4
p_c1_a4 = c1_a4 / t_per_area[3]
p_c2_a4 = c2_a4 / t_per_area[3]
p_c3_a4 = c3_a4 / t_per_area[3]
p_c4_a4 = c4_a4 / t_per_area[3]
p_c5_a4 = c5_a4 / t_per_area[3]
p_c6_a4 = c6_a4 / t_per_area[3]
# Area 5
p_c1_a5 = c1_a5 / t_per_area[4]
p_c2_a5 = c2_a5 / t_per_area[4]
p_c3_a5 = c3_a5 / t_per_area[4]
p_c4_a5 = c4_a5 / t_per_area[4]
p_c5_a5 = c5_a5 / t_per_area[4]
p_c6_a5 = c6_a5 / t_per_area[4]
# Area 6
p_c1_a6 = c1_a6 / t_per_area[5]
p_c2_a6 = c2_a6 / t_per_area[5]
p_c3_a6 = c3_a6 / t_per_area[5]
p_c4_a6 = c4_a6 / t_per_area[5]
p_c5_a6 = c5_a6 / t_per_area[5]
p_c6_a6 = c6_a6 / t_per_area[5]
# Area 7
p_c1_a7 = c1_a7 / t_per_area[6]
p_c2_a7 = c2_a7 / t_per_area[6]
p_c3_a7 = c3_a7 / t_per_area[6]
p_c4_a7 = c4_a7 / t_per_area[6]
p_c5_a7 = c5_a7 / t_per_area[6]
p_c6_a7 = c6_a7 / t_per_area[6]
# Area 8
p_c1_a8 = c1_a8 / t_per_area[7]
p_c2_a8 = c2_a8 / t_per_area[7]
p_c3_a8 = c3_a8 / t_per_area[7]
p_c4_a8 = c4_a8 / t_per_area[7]
p_c5_a8 = c5_a8 / t_per_area[7]
p_c6_a8 = c6_a8 / t_per_area[7]
# Area 9
p_c1_a9 = c1_a9 / t_per_area[8]
p_c2_a9 = c2_a9 / t_per_area[8]
p_c3_a9 = c3_a9 / t_per_area[8]
p_c4_a9 = c4_a9 / t_per_area[8]
p_c5_a9 = c5_a9 / t_per_area[8]
p_c6_a9 = c6_a9 / t_per_area[8]
# Area 10
p_c1_a10 = c1_a10 / t_per_area[9]
p_c2_a10 = c2_a10 / t_per_area[9]
p_c3_a10 = c3_a10 / t_per_area[9]
p_c4_a10 = c4_a10 / t_per_area[9]
p_c5_a10 = c5_a10 / t_per_area[9]
p_c6_a10 = c6_a10 / t_per_area[9]
# Area 11
p_c1_a11 = c1_a11 / t_per_area[10]
p_c2_a11 = c2_a11 / t_per_area[10]
p_c3_a11 = c3_a11 / t_per_area[10]
p_c4_a11 = c4_a11 / t_per_area[10]
p_c5_a11 = c5_a11 / t_per_area[10]
p_c6_a11 = c6_a11 / t_per_area[10]
# Area 12
p_c1_a12 = c1_a12 / t_per_area[11]
p_c2_a12 = c2_a12 / t_per_area[11]
p_c3_a12 = c3_a12 / t_per_area[11]
p_c4_a12 = c4_a12 / t_per_area[11]
p_c5_a12 = c5_a12 / t_per_area[11]
p_c6_a12 = c6_a12 / t_per_area[11]
# Area 13
p_c1_a13 = c1_a13 / t_per_area[12]
p_c2_a13 = c2_a13 / t_per_area[12]
p_c3_a13 = c3_a13 / t_per_area[12]
p_c4_a13 = c4_a13 / t_per_area[12]
p_c5_a13 = c5_a13 / t_per_area[12]
p_c6_a13 = c6_a13 / t_per_area[12]
# Area 14
p_c1_a14 = c1_a14 / t_per_area[13]
p_c2_a14 = c2_a14 / t_per_area[13]
p_c3_a14 = c3_a14 / t_per_area[13]
p_c4_a14 = c4_a14 / t_per_area[13]
p_c5_a14 = c5_a14 / t_per_area[13]
p_c6_a14 = c6_a14 / t_per_area[13]
# Area 15
p_c1_a15 = c1_a15 / t_per_area[14]
p_c2_a15 = c2_a15 / t_per_area[14]
p_c3_a15 = c3_a15 / t_per_area[14]
p_c4_a15 = c4_a15 / t_per_area[14]
p_c5_a15 = c5_a15 / t_per_area[14]
p_c6_a15 = c6_a15 / t_per_area[14]
# Area 16
p_c1_a16 = c1_a16 / t_per_area[15]
p_c2_a16 = c2_a16 / t_per_area[15]
p_c3_a16 = c3_a16 / t_per_area[15]
p_c4_a16 = c4_a16 / t_per_area[15]
p_c5_a16 = c5_a16 / t_per_area[15]
p_c6_a16 = c6_a16 / t_per_area[15]
# Area 17
p_c1_a17 = c1_a17 / t_per_area[16]
p_c2_a17 = c2_a17 / t_per_area[16]
p_c3_a17 = c3_a17 / t_per_area[16]
p_c4_a17 = c4_a17 / t_per_area[16]
p_c5_a17 = c5_a17 / t_per_area[16]
p_c6_a17 = c6_a17 / t_per_area[16]
# Area 18
p_c1_a18 = c1_a18 / t_per_area[17]
p_c2_a18 = c2_a18 / t_per_area[17]
p_c3_a18 = c3_a18 / t_per_area[17]
p_c4_a18 = c4_a18 / t_per_area[17]
p_c5_a18 = c5_a18 / t_per_area[17]
p_c6_a18 = c6_a18 / t_per_area[17]
# Area 19
p_c1_a19 = c1_a19 / t_per_area[18]
p_c2_a19 = c2_a19 / t_per_area[18]
p_c3_a19 = c3_a19 / t_per_area[18]
p_c4_a19 = c4_a19 / t_per_area[18]
p_c5_a19 = c5_a19 / t_per_area[18]
p_c6_a19 = c6_a19 / t_per_area[18]
# Area 20
p_c1_a20 = c1_a20 / t_per_area[19]
p_c2_a20 = c2_a20 / t_per_area[19]
p_c3_a20 = c3_a20 / t_per_area[19]
p_c4_a20 = c4_a20 / t_per_area[19]
p_c5_a20 = c5_a20 / t_per_area[19]
p_c6_a20 = c6_a20 / t_per_area[19]
# Area 21
p_c1_a21 = c1_a21 / t_per_area[20]
p_c2_a21 = c2_a21 / t_per_area[20]
p_c3_a21 = c3_a21 / t_per_area[20]
p_c4_a21 = c4_a21 / t_per_area[20]
p_c5_a21 = c5_a21 / t_per_area[20]
p_c6_a21 = c6_a21 / t_per_area[20]

#### Finding the dangers
d_a1 = t_per_area[0] * ((p_c1_a1 * sev1) +  (p_c2_a1 * sev2) +  (p_c3_a1 * sev3) +  (p_c4_a1 * sev4) +  (p_c5_a1 * sev5) +  (p_c6_a1 * sev6))
d_a2 = t_per_area[1] * ((p_c1_a2 * sev1) +  (p_c2_a2 * sev2) +  (p_c3_a2 * sev3) +  (p_c4_a2 * sev4) +  (p_c5_a2 * sev5) +  (p_c6_a2 * sev6))
d_a3 = t_per_area[2] * ((p_c1_a3 * sev1) +  (p_c2_a3 * sev2) +  (p_c3_a3 * sev3) +  (p_c4_a3 * sev4) +  (p_c5_a3 * sev5) +  (p_c6_a3 * sev6))
d_a4 = t_per_area[3] * ((p_c1_a4 * sev1) +  (p_c2_a4 * sev2) +  (p_c3_a4 * sev3) +  (p_c4_a4 * sev4) +  (p_c5_a4 * sev5) +  (p_c6_a4 * sev6))
d_a5 = t_per_area[4] * ((p_c1_a5 * sev1) +  (p_c2_a5 * sev2) +  (p_c3_a5 * sev3) +  (p_c4_a5 * sev4) +  (p_c5_a5 * sev5) +  (p_c6_a5 * sev6))
d_a6 = t_per_area[5] * ((p_c1_a6 * sev1) +  (p_c2_a6 * sev2) +  (p_c3_a6 * sev3) +  (p_c4_a6 * sev4) +  (p_c5_a6 * sev5) +  (p_c6_a6 * sev6))
d_a7 = t_per_area[6] * ((p_c1_a7 * sev1) +  (p_c2_a7 * sev2) +  (p_c3_a7 * sev3) +  (p_c4_a7 * sev4) +  (p_c5_a7 * sev5) +  (p_c6_a7 * sev6))
d_a8 = t_per_area[7] * ((p_c1_a8 * sev1) +  (p_c2_a8 * sev2) +  (p_c3_a8 * sev3) +  (p_c4_a8 * sev4) +  (p_c5_a8 * sev5) +  (p_c6_a8 * sev6))
d_a9 = t_per_area[8] * ((p_c1_a9 * sev1) +  (p_c2_a9 * sev2) +  (p_c3_a9 * sev3) +  (p_c4_a9 * sev4) +  (p_c5_a9 * sev5) +  (p_c6_a9 * sev6))
d_a10 = t_per_area[9] * ((p_c1_a10 * sev1) +  (p_c2_a10 * sev2) +  (p_c3_a10 * sev3) +  (p_c4_a10 * sev4) +  (p_c5_a10 * sev5) +  (p_c6_a10 * sev6))
d_a11 = t_per_area[10] * ((p_c1_a11 * sev1) +  (p_c2_a11 * sev2) +  (p_c3_a11 * sev3) +  (p_c4_a11 * sev4) +  (p_c5_a11 * sev5) +  (p_c6_a11 * sev6))
d_a12 = t_per_area[11] * ((p_c1_a12 * sev1) +  (p_c2_a12 * sev2) +  (p_c3_a12 * sev3) +  (p_c4_a12 * sev4) +  (p_c5_a12 * sev5) +  (p_c6_a12 * sev6))
d_a13 = t_per_area[12] * ((p_c1_a13 * sev1) +  (p_c2_a13 * sev2) +  (p_c3_a13 * sev3) +  (p_c4_a13 * sev4) +  (p_c5_a13 * sev5) +  (p_c6_a13 * sev6))
d_a14 = t_per_area[13] * ((p_c1_a14 * sev1) +  (p_c2_a14 * sev2) +  (p_c3_a14 * sev3) +  (p_c4_a14 * sev4) +  (p_c5_a14 * sev5) +  (p_c6_a14 * sev6))
d_a15 = t_per_area[14] * ((p_c1_a15 * sev1) +  (p_c2_a15 * sev2) +  (p_c3_a15 * sev3) +  (p_c4_a15 * sev4) +  (p_c5_a15 * sev5) +  (p_c6_a15 * sev6))
d_a16 = t_per_area[15] * ((p_c1_a16 * sev1) +  (p_c2_a16 * sev2) +  (p_c3_a16 * sev3) +  (p_c4_a16 * sev4) +  (p_c5_a16 * sev5) +  (p_c6_a16 * sev6))
d_a17 = t_per_area[16] * ((p_c1_a17 * sev1) +  (p_c2_a17 * sev2) +  (p_c3_a17 * sev3) +  (p_c4_a17 * sev4) +  (p_c5_a17 * sev5) +  (p_c6_a17 * sev6))
d_a18 = t_per_area[17] * ((p_c1_a18 * sev1) +  (p_c2_a18 * sev2) +  (p_c3_a18 * sev3) +  (p_c4_a18 * sev4) +  (p_c5_a18 * sev5) +  (p_c6_a18 * sev6))
d_a19 = t_per_area[18] * ((p_c1_a19 * sev1) +  (p_c2_a19 * sev2) +  (p_c3_a19 * sev3) +  (p_c4_a19 * sev4) +  (p_c5_a19 * sev5) +  (p_c6_a19 * sev6))
d_a20 = t_per_area[19] * ((p_c1_a20 * sev1) +  (p_c2_a20 * sev2) +  (p_c3_a20 * sev3) +  (p_c4_a20 * sev4) +  (p_c5_a20 * sev5) +  (p_c6_a20 * sev6))
d_a21 = t_per_area[20] * ((p_c1_a21 * sev1) +  (p_c2_a21 * sev2) +  (p_c3_a21 * sev3) +  (p_c4_a21 * sev4) +  (p_c5_a21 * sev5) +  (p_c6_a21 * sev6))

# Get all related values for each severity
# Severity 1
sev1_list = []
sev1_list.append(t_per_area[0]*(p_c1_a1))
sev1_list.append(t_per_area[1]*(p_c1_a2))
sev1_list.append(t_per_area[2]*(p_c1_a3))
sev1_list.append(t_per_area[3]*(p_c1_a4))
sev1_list.append(t_per_area[4]*(p_c1_a5))
sev1_list.append(t_per_area[5]*(p_c1_a6))
sev1_list.append(t_per_area[6]*(p_c1_a7))
sev1_list.append(t_per_area[7]*(p_c1_a8))
sev1_list.append(t_per_area[8]*(p_c1_a9))
sev1_list.append(t_per_area[9]*(p_c1_a10))
sev1_list.append(t_per_area[10]*(p_c1_a11))
sev1_list.append(t_per_area[11]*(p_c1_a12))
sev1_list.append(t_per_area[12]*(p_c1_a13))
sev1_list.append(t_per_area[13]*(p_c1_a14))
sev1_list.append(t_per_area[14]*(p_c1_a15))
sev1_list.append(t_per_area[15]*(p_c1_a16))
sev1_list.append(t_per_area[16]*(p_c1_a17))
sev1_list.append(t_per_area[17]*(p_c1_a18))
sev1_list.append(t_per_area[18]*(p_c1_a19))
sev1_list.append(t_per_area[19]*(p_c1_a20))
sev1_list.append(t_per_area[20]*(p_c1_a21))
# Severity 2
sev2_list = []
sev2_list.append(t_per_area[0]*(p_c2_a1))
sev2_list.append(t_per_area[1]*(p_c2_a2))
sev2_list.append(t_per_area[2]*(p_c2_a3))
sev2_list.append(t_per_area[3]*(p_c2_a4))
sev2_list.append(t_per_area[4]*(p_c2_a5))
sev2_list.append(t_per_area[5]*(p_c2_a6))
sev2_list.append(t_per_area[6]*(p_c2_a7))
sev2_list.append(t_per_area[7]*(p_c2_a8))
sev2_list.append(t_per_area[8]*(p_c2_a9))
sev2_list.append(t_per_area[9]*(p_c2_a10))
sev2_list.append(t_per_area[10]*(p_c2_a11))
sev2_list.append(t_per_area[11]*(p_c2_a12))
sev2_list.append(t_per_area[12]*(p_c2_a13))
sev2_list.append(t_per_area[13]*(p_c2_a14))
sev2_list.append(t_per_area[14]*(p_c2_a15))
sev2_list.append(t_per_area[15]*(p_c2_a16))
sev2_list.append(t_per_area[16]*(p_c2_a17))
sev2_list.append(t_per_area[17]*(p_c2_a18))
sev2_list.append(t_per_area[18]*(p_c2_a19))
sev2_list.append(t_per_area[19]*(p_c2_a20))
sev2_list.append(t_per_area[20]*(p_c2_a21))
# Severity 3
sev3_list = []
sev3_list.append(t_per_area[0]*(p_c3_a1))
sev3_list.append(t_per_area[1]*(p_c3_a2))
sev3_list.append(t_per_area[2]*(p_c3_a3))
sev3_list.append(t_per_area[3]*(p_c3_a4))
sev3_list.append(t_per_area[4]*(p_c3_a5))
sev3_list.append(t_per_area[5]*(p_c3_a6))
sev3_list.append(t_per_area[6]*(p_c3_a7))
sev3_list.append(t_per_area[7]*(p_c3_a8))
sev3_list.append(t_per_area[8]*(p_c3_a9))
sev3_list.append(t_per_area[9]*(p_c3_a10))
sev3_list.append(t_per_area[10]*(p_c3_a11))
sev3_list.append(t_per_area[11]*(p_c3_a12))
sev3_list.append(t_per_area[12]*(p_c3_a13))
sev3_list.append(t_per_area[13]*(p_c3_a14))
sev3_list.append(t_per_area[14]*(p_c3_a15))
sev3_list.append(t_per_area[15]*(p_c3_a16))
sev3_list.append(t_per_area[16]*(p_c3_a17))
sev3_list.append(t_per_area[17]*(p_c3_a18))
sev3_list.append(t_per_area[18]*(p_c3_a19))
sev3_list.append(t_per_area[19]*(p_c3_a20))
sev3_list.append(t_per_area[20]*(p_c3_a21))
# Severity 4
sev4_list = []
sev4_list.append(t_per_area[0]*(p_c4_a1))
sev4_list.append(t_per_area[1]*(p_c4_a2))
sev4_list.append(t_per_area[2]*(p_c4_a3))
sev4_list.append(t_per_area[3]*(p_c4_a4))
sev4_list.append(t_per_area[4]*(p_c4_a5))
sev4_list.append(t_per_area[5]*(p_c4_a6))
sev4_list.append(t_per_area[6]*(p_c4_a7))
sev4_list.append(t_per_area[7]*(p_c4_a8))
sev4_list.append(t_per_area[8]*(p_c4_a9))
sev4_list.append(t_per_area[9]*(p_c4_a10))
sev4_list.append(t_per_area[10]*(p_c4_a11))
sev4_list.append(t_per_area[11]*(p_c4_a12))
sev4_list.append(t_per_area[12]*(p_c4_a13))
sev4_list.append(t_per_area[13]*(p_c4_a14))
sev4_list.append(t_per_area[14]*(p_c4_a15))
sev4_list.append(t_per_area[15]*(p_c4_a16))
sev4_list.append(t_per_area[16]*(p_c4_a17))
sev4_list.append(t_per_area[17]*(p_c4_a18))
sev4_list.append(t_per_area[18]*(p_c4_a19))
sev4_list.append(t_per_area[19]*(p_c4_a20))
sev4_list.append(t_per_area[20]*(p_c4_a21))
# Severity 5
sev5_list = []
sev5_list.append(t_per_area[0]*(p_c5_a1))
sev5_list.append(t_per_area[1]*(p_c5_a2))
sev5_list.append(t_per_area[2]*(p_c5_a3))
sev5_list.append(t_per_area[3]*(p_c5_a4))
sev5_list.append(t_per_area[4]*(p_c5_a5))
sev5_list.append(t_per_area[5]*(p_c5_a6))
sev5_list.append(t_per_area[6]*(p_c5_a7))
sev5_list.append(t_per_area[7]*(p_c5_a8))
sev5_list.append(t_per_area[8]*(p_c5_a9))
sev5_list.append(t_per_area[9]*(p_c5_a10))
sev5_list.append(t_per_area[10]*(p_c5_a11))
sev5_list.append(t_per_area[11]*(p_c5_a12))
sev5_list.append(t_per_area[12]*(p_c5_a13))
sev5_list.append(t_per_area[13]*(p_c5_a14))
sev5_list.append(t_per_area[14]*(p_c5_a15))
sev5_list.append(t_per_area[15]*(p_c5_a16))
sev5_list.append(t_per_area[16]*(p_c5_a17))
sev5_list.append(t_per_area[17]*(p_c5_a18))
sev5_list.append(t_per_area[18]*(p_c5_a19))
sev5_list.append(t_per_area[19]*(p_c5_a20))
sev5_list.append(t_per_area[20]*(p_c5_a21))
# Severity 6
sev6_list = []
sev6_list.append(t_per_area[0]*(p_c6_a1))
sev6_list.append(t_per_area[1]*(p_c6_a2))
sev6_list.append(t_per_area[2]*(p_c6_a3))
sev6_list.append(t_per_area[3]*(p_c6_a4))
sev6_list.append(t_per_area[4]*(p_c6_a5))
sev6_list.append(t_per_area[5]*(p_c6_a6))
sev6_list.append(t_per_area[6]*(p_c6_a7))
sev6_list.append(t_per_area[7]*(p_c6_a8))
sev6_list.append(t_per_area[8]*(p_c6_a9))
sev6_list.append(t_per_area[9]*(p_c6_a10))
sev6_list.append(t_per_area[10]*(p_c6_a11))
sev6_list.append(t_per_area[11]*(p_c6_a12))
sev6_list.append(t_per_area[12]*(p_c6_a13))
sev6_list.append(t_per_area[13]*(p_c6_a14))
sev6_list.append(t_per_area[14]*(p_c6_a15))
sev6_list.append(t_per_area[15]*(p_c6_a16))
sev6_list.append(t_per_area[16]*(p_c6_a17))
sev6_list.append(t_per_area[17]*(p_c6_a18))
sev6_list.append(t_per_area[18]*(p_c6_a19))
sev6_list.append(t_per_area[19]*(p_c6_a20))
sev6_list.append(t_per_area[20]*(p_c6_a21))
#******************************************************
# List of all dangers (for each area)
danger_list = []
danger_list.append(d_a1)
danger_list.append(d_a2)
danger_list.append(d_a3)
danger_list.append(d_a4)
danger_list.append(d_a5)
danger_list.append(d_a6)
danger_list.append(d_a7)
danger_list.append(d_a8)
danger_list.append(d_a9)
danger_list.append(d_a10)
danger_list.append(d_a11)
danger_list.append(d_a12)
danger_list.append(d_a13)
danger_list.append(d_a14)
danger_list.append(d_a15)
danger_list.append(d_a16)
danger_list.append(d_a17)
danger_list.append(d_a18)
danger_list.append(d_a19)
danger_list.append(d_a20)
danger_list.append(d_a21)

# Combining the dependent (dangers) and independent (six types of crime)
write_list = []
for idx in range(len(danger_list)):
    templist = [danger_list[idx],sev1_list[idx],sev2_list[idx],sev3_list[idx],sev4_list[idx],sev5_list[idx],sev6_list[idx]]
    write_list.append(templist)

# Write the dangers and related severities to file for regression
with open(write_file,'w+',newline='') as weighted_file:
    csv_writer = csv.writer(weighted_file)
    header = ['Danger','Sev1','Sev2','Sev3','Sev4','Sev5','Sev6']
    csv_writer.writerow(header)
    for event in write_list:
        csv_writer.writerow(event)
