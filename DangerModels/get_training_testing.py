# This file divides master set into testing (20%) and training (80%)

import pandas
import random
import csv

###############################################
# Attempt with csv: Approx 80% training to 20% testing
###############################################

# Define file names
import_file = "master_data.csv"
export_training = "master_training.csv"
export_testing = "master_testing.csv"
with open(import_file) as i_file:
    with open(export_training, 'w+') as training:
        with open(export_testing, 'w+') as testing:
            header = next(i_file)
            training.write(header)
            testing.write(header)
            total_elements = 0
            # Assign each element to a dataset randomly
            for line in i_file:
                if total_elements > 500000:
                     break;
                if random.random() < .80:
                    training.write(line)
                else:
                    testing.write(line)
                total_elements += 1
# This is just a sanity check
print(total_elements)
###############################################
