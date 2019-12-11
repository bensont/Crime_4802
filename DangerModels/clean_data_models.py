# This specifically works for data from the LAPD Kaggle dataset https://www.kaggle.com/cityofLA/crime-in-los-angeles
#
# To run, put this file in the same directory as the csv file that needs to be
# weighted for severity, categorized for crime type, and classed on age. Then
# go to that directory in the terminal. Run the command: 'python clean_data.py'
# This will write to the file of your choosing. *Note* This will overwrite a
# file with the same name if it exists.
#
# To Clean Crime Data:
#
# Step One: Enter file name from which to read data
# Step Two: Enter file name to which to write the updated data
# Step Three: Execute
#
# Note: Search for 'read_file' for Step One and 'write_file' for Step Two input

import csv

# The list to be (re)written to the (new) file
write_list = []
################################################################################
################################################################################
# Step One (Insert name of file to be cleaned, for either training or testing)
# read_file = "master_training.csv"
read_file = "m_TRAINING_bestmodel.csv"
# Step Two (Insert name of file to output data with added weights and categories)
# Note: This will OVERWRITE the file with this name if it already exists!
write_file = "clean_best_training.csv"

traffic_weight = 0.0000147687
nonviolent_weight = 0.004328296
theft_weight = 0.016911184
sexual_weight = 0.000304396
child_weight = 0.000945535
violent_weight = 0.013554454
################################################################################
################################################################################
# Read file in
with open(read_file,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # All weighting, catigorizing, and classing is done per line to reduce runtime
    for line in csv_reader:
        #####################################################################
        # Assigning a category to each Crime code. The categories are:
        # 1: Traffic Related Crimes
        # 2: Non-Violent Crimes
        # 3: Theft and Robbery
        # 4: Sexual Crimes
        # 5: Child Victim Crimes
        # 6: Violent Crimes
        #
        # Some of these crimes can be classfied in multiple categories.
        # For example:
        # Rape is both violent and sexual
        # Armed Robbery is both violent and Theft
        # Again, we determined these categories to the best of our abilities and
        # narrowed down the categories into these primary six that neatly
        # encompass all crimes included in the data
        #
        # Creating lists of each type of crime. Each contains the crime codes
        # that belong in the category
        traffic_list = ['438','647','890','926']
        nonviolent_list = ['432','453','814','760','921','822','948','942','931','952','944','434','439','949','924','740','745','900','901','902','933','763','661','888','903','884','806','353','886','946']
        theft_list = ['210','445','475','652','470','472','220','349','347','350','345','450','446','354','310','320','510','487','520','330','331','341','653','343','668','950','951','473','662','649','660','654','670','471','474','664','651','420','410','421','440','441','444','442','443','666','433','480','485','351','352','451','452']
        sexual_list = ['830','805','810','815','821','820','840','850','932','762','956']
        child_list = ['920','910','922','235','627','812','870','865','954','237','880','813']
        violent_list = ['110','113','121','122','231','230','250','251','860','236','436','435','623','622','626','624','625','648','753','761','755','756','882','940','930','943','928','437']
        # Traffic Crimes
        if (line[7] in traffic_list):
            # Append severity for traffic crimes
            line.append(traffic_weight)
            # Append crime category ID
            line.append('1')
            # Append crime category description
            line.append('traffic')
        # Non Violent Crimes
        elif (line[7] in nonviolent_list):
            line.append(nonviolent_weight)
            line.append('2')
            line.append('nonviolent')
        # Theft and Robbery
        elif (line[7] in theft_list):
                line.append(theft_weight)
                line.append('3')
                line.append('theft')
        # Sexual
        elif (line[7] in sexual_list):
                line.append(sexual_weight)
                line.append('4')
                line.append('sexual')
        # Child
        elif (line[7] in child_list):
                line.append(child_weight)
                line.append('5')
                line.append('child')
        # Violent
        elif (line[7] in violent_list):
                line.append(violent_weight)
                line.append('6')
                line.append('violent')
        # The Crime Code hasn't been defined. It needs to be inserted into the correct if/elif statement
        else:
            print('Error: Cannot Assign Crime Category:',line[7],': ',line[8],'Please assign Crime Code category in clean_data.py')
            exit()

        ##################################################################
        # Dividing up the Victim ages in to meaninful age classes
        #
        #**************************************************************
        # NOTE: THE FOLLOWING FEATURE IS NOT YET AVAILABLE. I WILL ATTEMPT
        #       TO IMPLEMENT THIS FEATURE, TIME PERMITTING
        # This division can be set to be different ranges if desired
        # For example: Set delta to 10 for ten year division with 10,20,30,etc
        # Set delta to 15 for year division with 15,30,45,etc
        #
        # Set this variable to define age range
        # delta = 15
        # max_age = 115
        # if (line[10] < delta)
        #**************************************************************
        # If the age is not give, append a none value
        if (line[10] == ''):
            line.append(None)
        elif (line[10] < '15'):
            line.append(1)
        elif (line[10] >= '15' and line[10] < '30'):
            line.append(2)
        elif (line[10] >= '30' and line[10] < '45'):
            line.append(3)
        elif (line[10] >= '45' and line[10] < '60'):
            line.append(4)
        elif (line[10] >= '60' and line[10] < '75'):
            line.append(5)
        elif (line[10] >= '75' and line[10] < '90'):
            line.append(6)
        # Data only goes to 99
        else:
            line.append(7)

        # Add the appended line to the list to write out
        # This will have severity, category, and age class information included
        write_list.append(line)

    # Step Two (Insert name of file to output data with added weights and categories)
    # Note: This will OVERWRITE the file with this name if it already exists!
    with open(write_file,'w+',newline='') as weighted_file:
        csv_writer = csv.writer(weighted_file)
        header = ['DR Number','Date Reported','Date Occurred','Time Occurred','Area ID','Area Name','Reporting District','Crime Code','Crime Code Description','MO Codes','Victim Age','Victim Sex','Victim Descent','Premise Code','Premise Description','Weapon Used Code','Weapon Description','Status Code','Status Description','Crime Code 1','Crime Code 2','Crime Code 3','Crime Code 4','Address','Cross Street','Location','Severity','Crime Type Code','Crime Type','Age Class Code']
        csv_writer.writerow(header)
        for event in write_list:
            csv_writer.writerow(event)
