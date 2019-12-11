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
read_file = "./data_sets/master_data.csv"
# Step Two (Insert name of file to output data with added weights and categories)
# Note: This will OVERWRITE the file with this name if it already exists!
write_file = "./cleaned_data/master_cleaned.csv"
################################################################################
################################################################################
with open(read_file,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # All weighting, catigorizing, and classing is done per line to reduce runtime
    for line in csv_reader:
        #####################################################################
        # Assigning weights to each type of crime based on crime code and
        # the examination of the data. To be clear: I decided the weights
        # based on what I thought each crime's severity was compared to each
        # of ALL of the other crimes. Many have the same severity and there is
        # a large range.
        if (line[7] == '110'):
            line.append('8000')
        elif (line[7] == '121' or line[7] == '122' or line[7] == '920' or line[7] == '113'):
            line.append('5000')
        elif (line[7] == '435'):
            line.append('4500')
        elif (line[7] == '231'):
            line.append('4000')
        elif (line[7] == '230'):
            line.append('3800')
        elif (line[7] == '250' or line[7] == '251' or line[7] == '860' or line[7] == '910'):
            line.append('3500')
        elif (line[7] == '922'):
            line.append('2500')
        elif (line[7] == '236' or line[7] == '436' or line[7] == '623' or line[7] == '622'):
            line.append('2000')
        elif (line[7] == '926' or line[7] == '626' or line[7] == '624' or line[7] == '625' or line[7] == '648'):
            line.append('1500')
        elif (line[7] == '753'):
            line.append('1300')
        elif (line[7] == '761'):
            line.append('1000')
        elif (line[7] == '755' or line[7] == '756' or line[7] == '235'):
            line.append('800')
        elif (line[7] == '627'):
            line.append('600')
        elif (line[7] == '812' or line[7] == '870'):
            line.append('500')
        elif (line[7] == '830' or line[7] == '805' or line[7] == '882' or line[7] == '940'):
            line.append('300')
        elif (line[7] == '865' or line[7] == '930' or line[7] == '943' or line[7] == '210' or line[7] == '220'):
            line.append('200')
        elif (line[7] == '928' or line[7] == '350' or line[7] == '450'):
            line.append('150')
        elif (line[7] == '354' or line[7] == '310' or line[7] == '320'):
            line.append('120')
        elif (line[7] == '510' or line[7] == '487' or line[7] == '520'):
            line.append('100')
        elif (line[7] == '954' or line[7] == '237'  or line[7] == '668' or line[7] == '343' or line[7] == '330' or line[7] == '331' or line[7] == '341' or line[7] == '349' or line[7] == '653' or line[7] == '345' or line[7] == '347' or line[7] == '950'):
            line.append('80')
        elif (line[7] == '951' or line[7] == '473' or line[7] == '662' or line[7] == '649' or line[7] == '470' or line[7] == '437'):
            line.append('60')
        elif (line[7] == '948'  or line[7] == '664'  or line[7] == '810' or line[7] == '815' or line[7] == '660' or line[7] == '654' or line[7] == '670' or line[7] == '471' or line[7] == '472' or line[7] == '474' or line[7] == '644' or line[7] == '475' or line[7] == '438'):
            line.append('50')
        elif (line[7] == '651'):
            line.append('45')
        elif (line[7] == '420' or line[7] == '410' or line[7] == '446'):
            line.append('40')
        elif (line[7] == '421'):
            line.append('35')
        elif (line[7] == '440' or line[7] == '441' or line[7] == '652'):
            line.append('30')
        elif (line[7] == '444' or line[7] == '445' or line[7] == '821' or line[7] == '820' or line[7] == '840' or line[7] == '880' or line[7] == '813' or line[7] == '942' or line[7] == '931' or line[7] == '952' or line[7] == '944'):
            line.append('25')
        elif (line[7] == '434' or line[7] == '439' or line[7] == '850' or line[7] == '647' or line[7] == '932' or line[7] == '762' or line[7] == '956' or line[7] == '442' or line[7] == '443' or line[7] == '666'):
            line.append('20')
        elif (line[7] == '433' or line[7] == '480' or line[7] == '485' or line[7] == '351' or line[7] == '352' or line[7] == '451' or line[7] == '452' or line[7] == '949' or line[7] == '924' or line[7] == '740' or line[7] == '745' or line[7] == '900' or line[7] == '901' or line[7] == '902'):
            line.append('15')
        elif (line[7] == '933' or line[7] == '763' or line[7] == '661' or line[7] == '888' or line[7] == '903'):
            line.append('10')
        elif (line[7] == '432' or line[7] == '884' or line[7] == '806' or line[7] == '353' or line[7] == '886' or line[7] == '453'):
            line.append('5')
        elif (line[7] =='946' or line[7] == '890' or line[7] == '822' or line[7] == '921' or line[7] == '760' or line[7] == '814'):
            line.append('1')
        # The Crime Code hasn't been defined. It needs to be inserted into the correct if/elif statement
        else:
            print('Error: Cannot Assign Weight:',line[7],': ',line[8], 'Please assign Crime Code severity in clean_data.py')
            exit()
        #####################################################################
        # Assigning a category to each Crime code. The categories are:
        # 1: Traffic Related Crimes
        # 2: Non-Violent Crimes
        # 3: Theft and Robbery
        # 4: Sexual Crimes
        # 5: Child Victim Crimes
        # 6: Violent Crimes
        #
        # Some of these crimes can be classified in multiple categories.
        # For example:
        # Rape is both violent and sexual
        # Armed Robbery is both violent and Theft
        # Again, I determined these categories to the best of my abilities and
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
            line.append('1')
            line.append('traffic')
        # Non Violent Crimes
        elif (line[7] in nonviolent_list):
            line.append('2')
            line.append('nonviolent')
        # Theft and Robbery
        elif (line[7] in theft_list):
                line.append('3')
                line.append('theft')
        # Sexual
        elif (line[7] in sexual_list):
                line.append('4')
                line.append('sexual')
        # Child
        elif (line[7] in child_list):
                line.append('5')
                line.append('child')
        # Violent
        elif (line[7] in violent_list):
                line.append('6')
                line.append('violent')
        # The Crime Code hasn't been defined. It needs to be inserted into the correct if/elif statement
        else:
            print('Error: Cannot Assign Crime Category:',line[7],': ',line[8],'Please assign Crime Code category in clean_data.py')
            exit()

        ##################################################################
        # Dividing up the Victim ages in to meaningful age classes
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
