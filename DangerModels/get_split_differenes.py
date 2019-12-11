# This file finds the differences in calculated danger levels between each half
# of the training data. And finds the sum of differences to record for model
# comparision

# Define lists for
dangers_a = []
dangers_b = []
diffs = []
sum_diffs = 0
i = 0

dangers = []

read_file = "dangers_splits_model_1.csv"

# Open file with recorded splits
# Find the differences between each area and add to list
with open(read_file, 'r') as splita:
    next(splita)
    for line in splita:
        dangers.append(line)
    for line in dangers:
        dangers = line.split(",")
        first = float(dangers[0])
        second = float(dangers[1])
        diff = abs(float(first) - float(second))
        diffs.append(diff)
splita.close()

# Sum all the differences
for idx in diffs:
    sum_diffs += idx

# Print the sum of the differences and record for comparing against other models
print("Sum of differences: ", sum_diffs)
