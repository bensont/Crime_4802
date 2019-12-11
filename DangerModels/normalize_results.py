# This normalizes the final training and testing results to allow for
# comparision. Two types of normalization are done.

# Enter the results from the final modeling for training
danger_training = [234.5779173,262.7265032,420.407728,214.5543578,294.5635079,290.3077865,
                    265.8491273,270.4218895,306.1457071,276.4335031,315.1146323,446.8292339,
                    290.7206706,242.4235929,236.3842009,186.4388428,217.4040898,236.3953525,
                    215.6774004,125.6615275,105.6118547]

# Enter the results from the final modeling for testing
danger_testing = [58.44491663,66.40443705,106.1206497,52.96155786,72.14281898,71.40881602,
                    66.60372999,68.61652545,76.26062222,69.43166958,79.31691442,111.9697445,
                    72.3546456,60.01923965,59.83338971,46.69046541,55.6002104,57.71493757,
                    56.76705822,31.66919883,27.92886792]

# Find two types of normalization for training.
# 1) With the SUM of the dangers as the denominator
# 2) With the MAX of the dangers as the denominator
norm_1_training = [float(i)/sum(danger_training) for i in danger_training]
norm_2_training = [float(i)/max(danger_training) for i in danger_training]

# Find two types of normalization for testing.
# 1) With the SUM of the dangers as the denominator
# 2) With the MAX of the dangers as the denominator
norm_1_testing = [float(i)/sum(danger_testing) for i in danger_testing]
norm_2_testing = [float(i)/max(danger_testing) for i in danger_testing]

# Print the training/testing for SUM normalization
print("Normal - With Sum as Denom: \n")
print("Training: \n", norm_1_training)
print("Testing: \n", norm_1_testing)

# Print the training/testing for MAX normalization
print("Normal - With Max as Denom: \n")
print("Training: \n", norm_2_training)
print("Testing: \n",norm_2_testing,'\n')
