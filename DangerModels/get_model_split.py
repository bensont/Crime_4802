# Divide the training data into two equal training data sets with which
# to test models

# Define file names
import_file = "training_model_1.csv"
export_training = "training_splita.csv"
export_testing = "training_splitb.csv"
with open(import_file) as i_file:
    with open(export_training, 'w+') as traininga:
        with open(export_testing, 'w+') as trainingb:
            header = next(i_file)
            traininga.write(header)
            trainingb.write(header)
            total_elements = 0
            # Assign each element by mod 2 for equal distribution and write to files
            for line in i_file:
                if (total_elements%2 == 1):
                    traininga.write(line)
                else:
                    trainingb.write(line)
                total_elements += 1
